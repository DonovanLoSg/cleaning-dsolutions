import os
from dotenv import load_dotenv
import datetime
from bson import ObjectId
import pymongo
import flask_login
from flask import Flask, render_template, request, session, redirect, url_for, flash
# from passlib.hash import pbkdf2_sha256
import csv
import re


# load in the variables in the .env file into our operating system environment
load_dotenv()

app = Flask(__name__)


# connect to mongo
MONGO_URI = os.environ.get('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)

# define my db_name
DB_NAME = os.environ.get('DB_NAME')
USER_COLLECTION_NAME = os.environ.get('USER_COLLECTION_NAME')

# read in the SESSION_KEY variable from the operating system environment
SESSION_KEY = os.environ.get('SESSION_KEY')

# set the session key
app.secret_key = os.environ.get('SESSION_KEY')

# --- User Authentication: Start  ----------------------------
# create a login manager
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# User object
# This user object basically represents one user


class User(flask_login.UserMixin):
    pass


# user loader for the Flask-Login login manager
@login_manager.user_loader
def load_user(_id):
    # find the user from the database by its email
    user_data = client[DB_NAME][USER_COLLECTION_NAME].find_one({
        '_id': ObjectId(_id)
    })
    if user_data:
        # create a new user object
        current_user = User()
        current_user.id = str(user_data['_id'])
        current_user._id = str(user_data['_id'])
        current_user.email = user_data['email']
        current_user.nickname = user_data['nickname']
        current_user.admin = user_data['admin']
        return current_user
    else:
        return None


# encrypt user's password        <-- rmb to use your database to create a collection that stores registered users' info like passwords and emails
def password_encryptor(user_password):
    return pbkdf2_sha256.hash(user_password)

# verify user's password        <-- then use this function to check user's password against the password in your collection


def verify_password(user_input, encrypted_password):
    return pbkdf2_sha256.verify(user_input, encrypted_password)

# --- User Authentication: End ---------------------------------

# START ROUTING


# --------------------------------------------------
# Home Page
# --------------------------------------------------
@app.route('/')
def index():
    return redirect(url_for("home"))


@app.route('/home', methods=['GET', 'POST'])
def home():
    location_data = client[DB_NAME]['cleaning_locations'].find().sort(
        "location")
    random_articles = client[DB_NAME]['articles'].aggregate(
        [{"$sample": {"size": 5}}])
    if request.method == 'POST':  # recieved as form submitted
        current_user = load_user(session['_id'])
        form = request.form
        myQuery = {}
        tagsArray = []
        locationArray = []
        if form.getlist('check-search-titles') or form.getlist(
                'check-search-locations') or form.getlist('check-search-tags'):
            if form.getlist('check-search-titles'):
                if not(form.get('search-title') == ''):
                    search_article_string = re.escape(form.get('search-title'))
                    myQuery.update(
                        {'article_title': {'$regex': search_article_string, '$options': 'i'}})
                else:
                    flash(
                        'Please key in the words you want to search in the article titles.', 'info')
                    return render_template("/home.template.html", location_data=location_data, form=form, random_articles=random_articles)

            if form.getlist('check-search-locations'):
                locationArray = form.getlist('search-location')
                if len(locationArray) > 0:
                    myQuery.update(
                        {"cleaning_location": {"$in": locationArray}})
                else:
                    flash(
                        'Please key in the words you want to search in the article titles.', 'info')
                    return render_template("/home.template.html", location_data=location_data, form=form, random_articles=random_articles)

            if form.getlist('check-search-tags'):
                tagsArray = form.get('search-tags').strip().split(",")
                tagsArray = [item.lower().strip() for item in tagsArray]
                tagsArray = list(filter(None, tagsArray))
                if len(tagsArray) > 0:
                    myQuery.update(
                        {'tags': {'$elemMatch': {'$in': tagsArray}}})
                else:
                    flash('Please key in the tags you looking for.', 'info')
                    return render_template("/home.template.html", location_data=location_data, form=form, random_articles=random_articles)
        article_data = client[DB_NAME]['articles'].find(myQuery)
        return render_template("/articles/article-list.template.html", articles=article_data, listtype="search", form=form, tagsArray=tagsArray, locationArray=locationArray)
        # return render_template("home.template.html", form=form, location_data=location_data, myQuery = myQuery, article_data=article_data, tagsArray=tagsArray)
    else:
        return render_template("/home.template.html", location_data=location_data, random_articles=random_articles)


# --------------------------------------------------
# Login
# --------------------------------------------------
# Login Page
# accept email address and password
# successful verification will be shown a login successful message
# and redirect to home.
# unsuccessful verificaiton will be shown relevant error message
# and ask to retry


@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # recieved as form submitted
        form = request.form
        inputemail = form.get('input-email')
        inputpassword = form.get('input-password')
        # check email against database
        user_data = client[DB_NAME][USER_COLLECTION_NAME].find_one(
            {'email': inputemail})
        if user_data:
            # check email and password against database
            if user_data['password'] == inputpassword:
                # password correct
                tempid = str(ObjectId(user_data['_id']))
                logging_user = load_user(tempid)
                flask_login.login_user(logging_user)
                session['_id'] = logging_user._id
                session['nickname'] = logging_user.nickname
                session['admin'] = logging_user.admin
                current_user = load_user(ObjectId(session['_id']))
                flash(logging_user.nickname + 'logged in successfully.', 'success')
                return redirect(url_for('home'))
            else:
                # password incorrect
                flash('Password incorrect.', 'danger')
                return render_template("/auth/login.template.html", form=form)
        else:
            # no such email exist in database
            flash("User not found", category='danger')
            return render_template("/auth/login.template.html", form=form)

    else:
        # This template shows a login form,
        # only called if the request.method was not 'POST'.
        return render_template("/auth/login.template.html")


@ login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return render_template("/unauthorized.template.html")


# --------------------------------------------------
# Logout
# --------------------------------------------------
# A instruction to log the user out and return to the home page
@app.route('/auth/logout')
def logout():
    flash('User has successfully logged out.', category='danger')
    # session.pop('_id')
    # session.pop('nickname')
    # session.pop('admin')
    flask_login.logout_user()
    return redirect(url_for('home'))

# Registration form
# Allow an user to register for an account
# Redirect to login page after successful registration


@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = request.form
        # check whether the passwords are the same
        if not(form.get('input-password') == form.get('input-verify')):
            flash("The passwords do not match. Please retry.",
                  category='danger')
            return render_template("/auth/register.template.html", form=form)
        else:
            # check whether email is unique
            user_data = client[DB_NAME][USER_COLLECTION_NAME].find_one({
                'email': form.get('input-email')
            })
            if user_data:
                # Email address found in the database
                flash(
                    "This email address has been used for registration. " +
                    "Please use other email address", category='danger')
                return render_template("/auth/register.template.html",
                                       form=form)
            else:
                user_data = client[DB_NAME][USER_COLLECTION_NAME].insert_one({
                    'email': form.get('input-email'),
                    'nickname': form.get('input-nickname'),
                    'password': form.get('input-password'),
                    'admin': False}
                )
                flash("User registration successful. Please proceed to login.",
                      category='success')
                return render_template("/auth/login.template.html")
    else:
        # register form
        return render_template("/auth/register.template.html")


# --------------------------------------------------
# My Profile
# --------------------------------------------------
# Allow the user to view their own profile
# and update their nickanme and password
@app.route('/users/my-profile', methods=['GET', 'POST'])
@flask_login.login_required
def my_profile():
    if request.method == 'POST':
        form = request.form
        print(form)
        if form.get('input-password') == "":
            # no change in password, direct update nickname
            myquery = {'email': form.get('input-email')}
            updatevalues = {'$set': {'nickname': form.get('input-nickname')}}
            client[DB_NAME][USER_COLLECTION_NAME].update_one(
                myquery, updatevalues)
            flash("Profile successfully updated", category='success')
            return render_template("/users/my-profile.template.html",
                                   form=form)
        else:
            # changes to passowrd, to check both passwods to be the same
            # if both password are not the same
            if not(form.get('input-password') == form.get('input-verify')):
                # if the two passwords are not the same
                flash("The passwords do not match. Please retry.",
                      category='danger')
                return render_template("/users/my-profile.template.html",
                                       form=form)
            else:
                myquery = {'email': form.get('input-email')}
                updatevalues = {'$set': {'nickname': form.get(
                    'input-nickname'), 'password': form.get('input-password')}}
                client[DB_NAME][USER_COLLECTION_NAME].update_one(
                    myquery, updatevalues)
                flash("Profile successfully updated", category='success')
                return render_template("/users/my-profile.template.html",
                                       form=form)
    else:
        return render_template("/users/my-profile.template.html", current_user=flask_login.current_user)


@app.route('/about')
def about():
    return render_template("/about.template.html")


@app.route('/instructions')
def instructions():
    return render_template("/instructions.template.html")


# Allow user to select one of the articles by clicking
#  on the article titles from the search results
#  to view the article.
# Allow user to select one of the articles by clicking on
# the article titles from the list to view the article.
# Allow member to select one of the articles by clicking on
# the article titles from the list to view the article.
# Allow member to select one of the articles by clicking on
# the corresponding delete button.
# Allow member to delete the article by clicking on the
# delete confirmation button on the article itself.
# When a search is executed, it will return the result
# in a list containing article titles and cleaning locations.
# Allow administrator to select one of article by clicking
# on the article titles from the search results to view the article.
# Allow administrator to delete an article by clicking on the corresponding delete button.
# Allow administrator to delete any article.
@app.route('/articles/list')
def list_articles():
    return render_template("/articles/article-list.template.html")


@app.route('/articles/list-all')
def all_articles():
    myProjections = {"_id": 1, "article_title": 1, "cleaning_location": 1}
    articles = client[DB_NAME]['articles'].find(
        {}, myProjections).sort('date_modified', pymongo.DESCENDING)
    return render_template("/articles/article-list.template.html",
                           articles=articles, listtype='all')

# Display the article containing article titles,
# cleaning location, article content, cleaning items,
# cleaning supplies and tags.
# List the comments for individual articles
# Display the count of validating vote.
# Allow member to edit the article by clicking on the
# edit button on the article itself.
# Allow member to add a comment on the article page.
# Allow member to edit the comment he left
# on the article page
# Allow member to validate the article content by voting
# whether it works, somewhat works, or doesn’t work.
# Allow member to change their validating votes.
# Allow member to edit articles they contributed.
# Allow member to delete articles they contributed.
# Allow administrator to delete an article by clicking on the delete button on the article itself.
# Allow administrator to edit an article by clicking on the edit button on the article itself.
# Allow administrator to add a comment on the article page.
# Allow member to edit the comment he left on the article page.
# Allow administrator to validate the article content by voting
#  whether it works, somewhat works, or doesn’t work.
# Allow administrator to change their validating votes.
# Allow administrator to edit any article.


@app.route('/articles/<_id>')
def show_article(_id):
    if (_id != "") :
        myQuery1 = {'_id': ObjectId(_id)}
        article_data = client[DB_NAME]['articles'].find_one(myQuery1)
        if (article_data):
            article_owner_id = article_data['created_by']
            myQuery2 = {'_id': article_owner_id}
            article_owner_data = client[DB_NAME][USER_COLLECTION_NAME].find_one(myQuery2)
            
            return render_template("/articles/article.template.html", article_data=article_data, article_id=_id, 
            article_owner_data=article_owner_data)
        else:
            flash('No such article found', category='danger')
            return redirect(url_for('home'))
    else:
        flash('No such article found', category='danger')
        return redirect(url_for('home'))


@app.route('/articles/edit/<_id>', methods=['GET', 'POST'])
@flask_login.login_required
def edit_article(_id):
    current_user = load_user(session['_user_id'])
    myQuery1 = {'_id': ObjectId(_id)}
    article_data = client[DB_NAME]['articles'].find_one(myQuery1)
    if (article_data):
        article_owner_id = article_data['created_by']
        myQuery2 = {'_id': article_owner_id}
        article_owner_data = client[DB_NAME][USER_COLLECTION_NAME].find_one(myQuery2)
        article_owner_id = article_data['created_by']
        if (article_owner_id == current_user.id or current_user.admin):
            location_data = client[DB_NAME]['cleaning_locations'].find().sort("location")
            if request.method == 'GET':
                return render_template("/articles/edit.template.html", location_data=location_data, article_id=_id, article_owner_data=article_owner_data, current_user=current_user, article_data=article_data)
            else:
                return "post method"
        else:
            flash('Unauthorised access', category='danger')
            return redirect(url_for('home'))
    else:
        flash('No such article found', category='danger')
        return redirect(url_for('home'))




@app.route('/articles/delete/<_id>')
@flask_login.login_required
def delete_article(_id):
    if not(_id is None) and ObjectId.is_valid(_id):
        myQuery1 = {'_id': ObjectId(_id)}
        article_data = client[DB_NAME]['articles'].find_one(myQuery1)
        if (article_data):
            article_owner_id = article_data['created_by']
            myQuery2 = {'_id': ObjectId(article_owner_id)}
            article_owner_data = client[DB_NAME][USER_COLLECTION_NAME].find_one(
                myQuery2)
            if '_user_id' in session:
                current_user = load_user(session['_user_id'])
            else:
                current_user = None
            return render_template("/articles/delete.template.html", article_data=article_data, article_id=_id, article_owner_data=article_owner_data, current_user=current_user)
        else:
            flash('No such article found', category='danger')
            return redirect(url_for('home'))
    else:
        flash('No such article found', category='danger')
        return redirect(url_for('home'))




# Display a list of all articles the member contributed.
# Allow member to select one of the articles by clicking on
# the article titles from the list to view the article.
# Allow member to select one of the articles by clicking on
# the corresponding delete button.
# Allow member to delete the article by clicking on the
# delete confirmation button on the article itself.
# Allow administrator to select one of article by clicking
# on the article titles from the search results to view the article.
# Allow administrator to delete an article by clicking on the corresponding delete button.
# Allow administrator to delete any article.
@app.route('/articles/my-list')
@flask_login.login_required
def my_articles():
    myQuery = {'created_by': ObjectId(session['_user_id'])}
    myProjections = {"_id": 1, "article_title": 1, "cleaning_location": 1}
    articles = client[DB_NAME]['articles'].find(
        myQuery, myProjections).sort('date_modified', pymongo.DESCENDING)
    return render_template("/articles/article-list.template.html",
                           articles=articles, listtype='my')


# Include an article creation page accepting article titles,
# cleaning location, article content, cleaning items,
# cleaning supplies and tags.
# Include an article creation page accepting article titles,
#  cleaning location, article content, cleaning items, cleaning supplies and tags.


@app.route('/articles/contribute', methods=['GET', 'POST'])
@flask_login.login_required
def contribute_articles():
    location_data = client[DB_NAME]['cleaning_locations'].find().sort(
        "location")
    if request.method == 'POST':
        form = request.form
        input_title = request.form.get('input-title')
        input_location = form.get('input-location')
        input_content = form.get('input-content')
        input_items = form.get("input-items").split(",")
        input_items = [item.strip(' ') for item in input_items]
        input_supplies = form.get("input-supplies").split(",")
        input_supplies = [item.strip(' ') for item in input_supplies]
        input_tags = form.get("input-tags").split(",")
        input_tags = [item.strip(' ') for item in input_tags]
        now = datetime.datetime.now()
        input_created = now.strftime('%y-%m-%d %a %H:%M')
        input_modified = now.strftime('%y-%m-%d %a %H:%M')
        input_creator = ObjectId(session['_user_id'])

        client[DB_NAME]['articles'].insert_one({
            'article_title': input_title,
            'cleaning_location': input_location,
            'article_content': input_content,
            'cleaning_items': input_items,
            'cleaning_supplies': input_supplies,
            'tags': input_tags,
            'last_modified': input_modified,
            'date_created': input_created,
            'created_by': input_creator
        })

        # .save({
        #     'artic1e_tit1e': form.get("input-title"),
        #     'c1eaning_location': form.get("input_location"),
        #     'article_content': form.get("input-content"),
        #     'cleaning_items': form.getlist("input-items"),
        #     'cleaning_supplies': form.getlist("input-supplies"),
        #     'tags': form.getlist("input-tags"),
        #     'last_modified': datetime.datetime.utcnow(),
        #     'last_created': datetime.datetime.utcnow(),
        #     'created_by': session.id})
        # flash('Article successfully submitted', category='success')
        # return render_template("/articles/contribute.template.html", location_data=location_data, form=form)
        return render_template("/articles/contribute-next.template.html", location_data=location_data, form=form)
    else:
        return render_template("/articles/contribute.template.html", location_data=location_data)



# --------------------------------------------------
# Cleaning Locations
# --------------------------------------------------
# Allow administrator to manage the list of cleaning location.
@app.route('/cleaning-locations/manage', methods=['GET', 'POST'])
@flask_login.login_required
def manage_cleaning_locations():
    if request.method == 'POST':
        form = request.form
        location_data = client[DB_NAME]['cleaning_locations'].find_one(
            {'_id': ObjectId(form.get('id'))})
        # render a form to allow editing of the selectedd cleaning location
        if form.get('action') == "edit":
            return render_template("/cleaning-locations/edit.template.html",
                                   location_data=location_data)
        # update the database with the changes to
        # the selected cleaning location
        elif form.get('action') == "edit-process":
            myquery = {'_id': ObjectId(form.get('id'))}
            updatevalues = {'$set': {'location': form.get('input-location')}}
            client[DB_NAME]['cleaning_locations'].update_one(
                myquery, updatevalues)
            flash('Location successfully updated', category='success')
            return redirect("/cleaning-locations/manage")
        # display the record mark for deletion to ask for confirmation
        elif form.get('action') == "delete":
            return render_template("/cleaning-locations/delete.template.html",
                                   location_data=location_data)
        # remove the selected clearning location from the database
        elif form.get('action') == "delete-process":
            myquery = {'_id': ObjectId(form.get('id'))}
            client[DB_NAME]['cleaning_locations'].delete_one(myquery)
            flash('Location successfully deleted', category='success')
            return redirect("/cleaning-locations/manage")
        # Insert the new cleaning location into the database
        elif form.get('action') == "add":
            client[DB_NAME]['cleaning_locations'].insert_one(
                {'location': form.get('input-new-location')})
            flash("New cleaning location added.")
            return redirect("/cleaning-locations/manage")
        else:
            return redirect(url_for('error_encountered'))
    else:
        # display the add cleaning location form and
        # list out the cleaning locations in the databasse
        location_data = client[DB_NAME]['cleaning_locations'].find().sort(
            'location', pymongo.ASCENDING)
        return render_template("/cleaning-locations/manage.template.html",
                               location_data=location_data)

# --------------------------------------------------
# Users Administration
# --------------------------------------------------
# Allow administrators to manage the list of users.


@app.route('/users/manage', methods=['GET', 'POST'])
@flask_login.login_required
def manage_users():
    if request.method == 'POST':
        form = request.form
        user_data = client[DB_NAME][USER_COLLECTION_NAME].find_one(
            {'_id': ObjectId(form.get('id'))})
        # Render a form to allow editing of the selected user
        # This includes changing nickname, reset password and
        # assigning administrator's rights
        if form.get('action') == 'edit':
            return render_template("/users/edit.template.html",
                                   form=form, user_data=user_data)
        # update the database with the changes to the selected user
        elif form.get('action') == 'edit-process':
            if form.get('input-password') == "":
                if form.get('input-admin') == 'isAdmin':
                    adminrights = True
                else:
                    adminrights = False
                # no change in password, direct update nickname and/or admin
                myquery = {'_id': ObjectId(form.get('id'))}
                updatevalues = {'$set': {'nickname': form.get(
                    'input-nickname'), 'admin': adminrights}}
                client[DB_NAME][USER_COLLECTION_NAME].update_one(
                    myquery, updatevalues)
                flash("User details successfully updated", category='success')
                return render_template("/users/edit.template.html",
                                       form=form, user_data=user_data)
            else:
                if not(form.get('input-password') == form.get('input-verify')):
                    flash("The passwords do not match. Please retry.",
                          category='danger')
                    return render_template("/users/edit.template.html",
                                           form=form, user_data=user_data)
                else:
                    myquery = {'_id': ObjectId(form.get('id'))}
                    if form.get('input-admin') == 'isAdmin':
                        adminrights = True
                    else:
                        adminrights = False
                    updatevalues = {'$set': {
                        'nickname': form.get('input-nickname'),
                        'password': form.get('input-password'),
                        'admin': adminrights}}
                    client[DB_NAME][USER_COLLECTION_NAME].update_one(
                        myquery, updatevalues)
                    flash("Profile successfully updated", category='success')
                    return render_template("/users/edit.template.html",
                                           form=form, user_data=user_data)
        # display the record mark for deletion to ask for confirmation
        elif form.get('action') == 'delete':
            return render_template("/users/delete.template.html",
                                   form=form, user_data=user_data)
        # remove the selected user from the database
        elif form.get('action') == "delete-process":
            myquery = {'_id': ObjectId(form.get('id'))}
            client[DB_NAME][USER_COLLECTION_NAME].delete_one(myquery)
            flash('User successfully deleted', category='success')
            return redirect("/users/manage")
        else:
            return redirect(url_for('error_encountered'))
    else:
        # display the search box and list out the users in the databasse
        user_data = client[DB_NAME][USER_COLLECTION_NAME].find().sort(
            'nickname', pymongo.ASCENDING)
        return render_template("/users/manage.template.html",
                               user_data=user_data)


# inbuilt function which handles exception like file not found
@app.errorhandler(404)
def not_found(e):
    return redirect(url_for("home"))


@app.route('/error-encountered')
def error_encountered():
    return render_template('/error-encountered.template.html')


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
