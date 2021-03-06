import os
from dotenv import load_dotenv
import datetime
from bson import ObjectId
import pymongo
import flask_login
from flask import Flask, render_template, request
from flask import session, redirect, url_for, flash
import re

# load in the variables in the .env file into our operating system environment
load_dotenv()

app = Flask(__name__)


# connect to mongoa
MONGO_URI = os.environ.get('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)

# define my DB_NAME
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_LOCATION = os.environ.get('DB_LOCATION')
DB_ARTICLE = os.environ.get('DB_ARTICLE')

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
    user_data = client[DB_NAME][DB_USER].find_one({
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

# --- User Authentication: End ---------------------------------

# START ROUTING

# --------------------------------------------------
# Home Page
# --------------------------------------------------


@app.route('/')
def index():
    location_data = client[DB_NAME][DB_LOCATION].find().sort(
        "location")
    random_articles = client[DB_NAME][DB_ARTICLE].aggregate(
        [{"$sample": {"size": 5}}])

    return render_template(
           "/index.template.html",
           location_data=location_data,
           random_articles=random_articles)


@app.route('/home', methods=['GET', 'POST'])
def home():

    random_articles = client[DB_NAME][DB_ARTICLE].aggregate(
        [{"$sample": {"size": 5}}])
    if request.method == 'POST':  # recieved as form submitted
        form = request.form
        myQuery = {}
        tagsArray = []
        locationArray = []
        if ((form.getlist('check-search-titles')
             and form.get('search-title') != '')
            or (form.getlist('check-search-locations')
                and form.getlist('check-search-locations') != '')
            or (form.getlist('check-search-tags')
                and form.getlist('check-search-tags') != '')):
            if form.getlist('check-search-titles'):
                if form.getlist('check-search-titles') != '':
                    search_article_string = re.escape(form.get('search-title'))
                    myQuery.update(
                        {'article_title': {'$regex':
                                           search_article_string,
                                           '$options': 'i'}})
                else:
                    flash(
                        'Please key in the words you want to search'
                        'in the article titles.', 'info')
                    location_data = client[DB_NAME][DB_LOCATION].find().sort(
                        "location")
                    return render_template("/home.template.html",
                                           location_data=location_data,
                                           form=form,
                                           random_articles=random_articles)

            if form.getlist('check-search-locations'):
                locationArray = form.getlist('search-location')
                if len(locationArray) > 0:
                    myQuery.update(
                        {"cleaning_location": {"$in": locationArray}})
                else:
                    flash('Please select the location'
                          'you want to read about.', 'info')
                    location_data = client[DB_NAME][DB_LOCATION].find().sort(
                        "location")
                    return render_template("/home.template.html",
                                           location_data=location_data,
                                           form=form,
                                           random_articles=random_articles)

            if form.getlist('check-search-tags'):
                tagsArray = form.get('search-tags').strip().split(",")
                tagsArray = [item.lower().strip() for item in tagsArray]
                tagsArray = list(filter(None, tagsArray))
                if len(tagsArray) > 0:
                    myQuery.update(
                        {'tags': {'$elemMatch': {'$in': tagsArray}}})
                else:
                    flash('Please key in the tags you looking for.', 'info')
                    location_data = client[DB_NAME][DB_LOCATION].find().sort(
                        "location")
                    return render_template("/home.template.html",
                                           location_data=location_data,
                                           form=form,
                                           random_articles=random_articles)
        else:
            flash('Please select at least one search criteria.', 'info')
            location_data = client[DB_NAME][DB_LOCATION].find().sort(
                "location")
            return render_template("/home.template.html",
                                   location_data=location_data,
                                   form=form,
                                   random_articles=random_articles)
        article_data = client[DB_NAME][DB_ARTICLE].find(myQuery)
        return render_template("/articles/article-list.template.html",
                               articles=article_data,
                               listtype="search",
                               form=form,
                               tagsArray=tagsArray,
                               locationArray=locationArray)
    else:
        location_data = client[DB_NAME][DB_LOCATION].find().sort("location")
        return render_template("/home.template.html",
                               location_data=location_data,
                               random_articles=random_articles,
                               )


@app.route('/about')
def about():
    return redirect('https://support.cleaning.dsolutions.sg/about')


@app.route('/instructions')
def instructions():
    return redirect('https://support.cleaning.dsolutions.sg/')


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
        user_data = client[DB_NAME][DB_USER].find_one(
            {'email': inputemail})
        if user_data:
            # check email and password against database
            if inputpassword == user_data['password']:
                # password correct
                tempid = str(ObjectId(user_data['_id']))
                logging_user = User()
                logging_user = load_user(tempid)
                flask_login.login_user(logging_user)
                session['_id'] = logging_user.get_id()
                session['nickname'] = logging_user.nickname
                session['admin'] = logging_user.admin
                flash(logging_user.nickname
                      + ' logged in successfully.', 'success')
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


# --------------------------------------------------
# Logout
# --------------------------------------------------
# A instruction to log the user out and return to the home page
@app.route('/auth/logout')
def logout():
    flash('User has successfully logged out.', category='danger')
    session.pop('_id', None)
    session.pop('nickname', None)
    session.pop('admin', None)
    flask_login.logout_user()
    return redirect(url_for('home'))


# --------------------------------------------------
# Handling unauthorized user
# --------------------------------------------------

@ login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return render_template("/unauthorized.template.html")


# --------------------------------------------------
# Registration form
# --------------------------------------------------
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
            user_data = client[DB_NAME][DB_USER].find_one({
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
                user_data = client[DB_NAME][DB_USER].insert_one({
                    'email': form.get('input-email'),
                    'nickname': form.get('input-nickname'),
                    'password': form.get('input-password'),
                    'admin': False}
                )
                flash("User registration successful. Please proceed to login.",
                      category='success')
                return redirect(url_for('login'))
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
    current_user = load_user(flask_login.current_user.get_id())
    if request.method == 'POST':
        form = request.form
        print(form)
        if form.get('input-password') == "":
            # no change in password, direct update nickname
            myquery = {'email': form.get('input-email')}
            updatevalues = {'$set': {'nickname': form.get('input-nickname')}}
            client[DB_NAME][DB_USER].update_one(
                myquery, updatevalues)
            flash("Profile successfully updated", category='success')
            return render_template("/users/my-profile.template.html",
                                   form=form)
        else:
            # changes to passowrd, to check both passwods to be the same
            # if both password are not the same
            if form.get('input-password') != form.get('input-verify'):
                # if the two passwords are not the same
                flash("The passwords do not match. Please retry.",
                      category='danger')
                return render_template("/users/my-profile.template.html",
                                       form=form)
            else:
                myquery = {'email': form.get('input-email')}
                updatevalues = {'$set': {'nickname': form.get(
                    'input-nickname'), 'password': form.get('input-password')}}
                client[DB_NAME][DB_USER].update_one(
                    myquery, updatevalues)
                flash("Profile successfully updated", category='success')
                return render_template("/users/my-profile.template.html",
                                       form=form)
    else:
        return render_template("/users/my-profile.template.html",
                               current_user=current_user)


# --------------------------------------------------
# Article Listing
# --------------------------------------------------
# List all articles or articles from a search result
# Allow the user to view an article
# by clicking on the View button
# Allow the member or admin to delete an article
# by clicking on the Delete button

@app.route('/articles/list')
def list_articles():
    return redirect(url_for('all_articles'))


@app.route('/articles/list-all')
def all_articles():
    current_user = load_user(flask_login.current_user.get_id())
    myProjections = {"_id": 1, "article_title": 1, "cleaning_location": 1}
    articles = client[DB_NAME][DB_ARTICLE].find(
        {}, myProjections).sort('date_modified', pymongo.DESCENDING)
    return render_template("/articles/article-list.template.html",
                           articles=articles,
                           listtype='all',
                           current_user=current_user)


# --------------------------------------------------
# My Articles
# --------------------------------------------------
# Display a list of articles the member has contributed.
# The member can view an article or delete an article

@app.route('/articles/my-list')
@flask_login.login_required
def my_articles():
    current_user = load_user(flask_login.current_user.get_id())
    myQuery = {'created_by': ObjectId(current_user._id)}
    myProjections = {"_id": 1, "article_title": 1, "cleaning_location": 1}
    articles = client[DB_NAME][DB_ARTICLE].find(
        myQuery, myProjections).sort('date_modified', pymongo.DESCENDING)
    return render_template("/articles/article-list.template.html",
                           current_user=current_user,
                           articles=articles,
                           listtype='my')


# --------------------------------------------------
# Contribute Article
# --------------------------------------------------
# Display a form that allow the registered member to contribute their articles


@app.route('/articles/contribute', methods=['GET', 'POST'])
@flask_login.login_required
def contribute_articles():
    location_data = client[DB_NAME][DB_LOCATION].find().sort(
        "location")
    current_user = load_user(flask_login.current_user.get_id())
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
        now = datetime.datetime.utcnow()
        input_created = now.strftime('%y-%m-%d %a %H:%M')
        input_modified = now.strftime('%y-%m-%d %a %H:%M')
        input_creator = ObjectId(current_user._id)
        input_user_postings = [{'_id': ObjectId(), 'user_id': '0',
                                'good_rating': False, 'neutral_rating': False,
                                'bad_rating': False, 'comments': ""}]
        input_user_postings = []
        client[DB_NAME][DB_ARTICLE].insert_one({
            'article_title': input_title,
            'cleaning_location': input_location,
            'article_content': input_content,
            'cleaning_items': input_items,
            'cleaning_supplies': input_supplies,
            'tags': input_tags,
            'last_modified': input_modified,
            'date_created': input_created,
            'created_by': input_creator,
            'user_postings': input_user_postings
        })

        flash('Article successfully submitted', category='success')
        return render_template("/articles/contribute-next.template.html",
                               location_data=location_data, form=form)
    else:
        return render_template("/articles/contribute.template.html",
                               location_data=location_data)

# --------------------------------------------------
# Edit Article
# --------------------------------------------------
# Display a form that allow the registered member to contribute their articles


@app.route('/articles/edit/<_id>', methods=['GET', 'POST'])
@flask_login.login_required
def edit_article(_id):
    current_user = load_user(flask_login.current_user.get_id())
    myQuery1 = {'_id': ObjectId(_id)}
    article_data = client[DB_NAME][DB_ARTICLE].find_one(myQuery1)
    if (article_data):
        article_owner_id = str(article_data['created_by'])
        myQuery2 = {'_id': ObjectId(article_owner_id)}
        article_owner_data = client[DB_NAME][DB_USER].find_one(myQuery2)
        article_owner_id = str(article_data['created_by'])
        if (article_owner_id == current_user._id) or current_user.admin:
            location_data = client[DB_NAME][DB_LOCATION].find()
            location_data.sort("location")
            if request.method == 'GET':
                return render_template("/articles/edit.template.html",
                                       location_data=location_data,
                                       article_id=_id,
                                       article_owner_data=article_owner_data,
                                       current_user=current_user,
                                       article_data=article_data)
            else:
                form = request.form
                input_title = request.form.get('input-title')
                input_location = form.get('input-location')
                input_content = form.get('input-content')
                input_items = form.get("input-items").split(",")
                input_items = [item.strip(' ') for item in input_items]
                while ("" in input_items):
                    input_items.remove("")
                input_supplies = form.get("input-supplies").split(",")
                input_supplies = [item.strip(' ') for item in input_supplies]
                while ("" in input_supplies):
                    input_supplies.remove("")
                input_tags = form.get("input-tags").split(",")
                input_tags = [item.strip(' ') for item in input_tags]
                while ("" in input_tags):
                    input_tags.remove("")
                now = datetime.datetime.utcnow()
                input_modified = now.strftime('%y-%m-%d %a %H:%M')
                client[DB_NAME][DB_ARTICLE].update_one({
                    '_id': article_data['_id']}, {'$set': {
                        'article_title': input_title,
                        'cleaning_location': input_location,
                        'article_content': input_content,
                        'cleaning_items': input_items,
                        'cleaning_supplies': input_supplies,
                        'tags': input_tags,
                        'last_modified': input_modified}})
                flash('Article saved', category='success')
                return redirect(url_for('show_article', _id=_id))
        else:
            flash('Unauthorised access', category='danger')
            return redirect(url_for('home'))
    else:
        flash('No such article found', category='danger')
        return redirect(url_for('home'))


# --------------------------------------------------
# Show Article
# --------------------------------------------------
# Display of the selected article, the total number of rating,
# a link to view comments.
# There will be Edit and Delete button for
# the owner of the article and the admin
# A registered member will be able to rate
# and leave comments or edit his own comments.


@app.route('/articles/<_id>')
def show_article(_id):
    if (_id != ""):
        myQuery1 = {'_id': ObjectId(_id)}
        current_user = load_user(flask_login.current_user.get_id())
        article_data = client[DB_NAME][DB_ARTICLE].find_one(myQuery1)
        if (article_data):
            article_owner_id = str(article_data['created_by'])
            myQuery2 = {'_id': ObjectId(article_owner_id)}
            article_owner_data = client[DB_NAME][DB_USER].find_one(myQuery2)
            user_posting_data = client[DB_NAME][DB_ARTICLE].find(
                {'_id': ObjectId(_id)},
                {'user_postings.user_id': 1,
                 'user_postings.good_rating': 1,
                 'user_postings.neutral_rating': 1,
                 'user_postings.bad_rating': 1,
                 'user_postings.comments': 1})
            user_posting_data.rewind()
            user_posting_list = list(user_posting_data)
            user_postings = user_posting_list[0]['user_postings']
            user_posting_data.rewind()
            good_rating_count = 0
            neutral_rating_count = 0
            bad_rating_count = 0
            user_rated = ''
            user_comments = ''
            for post in user_postings:
                if post['user_id'] != "0":
                    if current_user:
                        if post['user_id'] == ObjectId(current_user._id):
                            if post['good_rating']:
                                user_rated = 'good'
                            if post['neutral_rating']:
                                user_rated = 'neutral'
                            if post['bad_rating']:
                                user_rated = 'bad'
                            user_comments = post['comments']
                        if post['good_rating']:
                            good_rating_count = good_rating_count + 1
                        if post['neutral_rating']:
                            neutral_rating_count = neutral_rating_count + 1
                        if post['bad_rating']:
                            bad_rating_count = bad_rating_count + 1
            return render_template("/articles/article.template.html",
                                   current_user=current_user,
                                   article_data=article_data,
                                   article_id=_id,
                                   article_owner_id=article_owner_id,
                                   article_owner_data=article_owner_data,
                                   user_postings=user_postings,
                                   good_rating_count=good_rating_count,
                                   neutral_rating_count=neutral_rating_count,
                                   bad_rating_count=bad_rating_count,
                                   user_rated=user_rated,
                                   user_comments=user_comments)

        else:
            flash('No such article found', category='danger')
            return redirect(url_for('home'))
    else:
        flash('No such article found', category='danger')
        return redirect(url_for('home'))


# --------------------------------------------------
# Delete Article
# --------------------------------------------------
# Display of the selected article and seek confirmation


@app.route('/articles/delete/<_id>/<listtype>', methods=['GET', 'POST'])
@flask_login.login_required
def delete_article(_id, listtype):
    current_user = load_user(flask_login.current_user.get_id())
    if request.method == 'GET':
        if not(_id is None) and ObjectId.is_valid(_id):
            myQuery1 = {'_id': ObjectId(_id)}
            article_data = client[DB_NAME][DB_ARTICLE].find_one(myQuery1)
            if (article_data):
                article_owner_id = str(article_data['created_by'])
                myQuery2 = {'_id': ObjectId(article_owner_id)}
                article_owner_data = client[DB_NAME][DB_USER].find_one(
                                     myQuery2)
                if '_user_id' in session:
                    current_user = load_user(flask_login.current_user.get_id())
                else:
                    current_user = None
                return render_template("/articles/delete.template.html",
                                       article_data=article_data,
                                       article_id=_id,
                                       article_owner_id=article_owner_id,
                                       article_owner_data=article_owner_data,
                                       current_user=current_user,
                                       listtype=listtype)
            else:
                flash('No such article found', category='danger')
                return redirect(url_for('home'))
        else:
            flash('No such article found', category='danger')
            return redirect(url_for('home'))
    else:
        myQuery1 = {'_id': ObjectId(_id)}
        article_data = client[DB_NAME][DB_ARTICLE].delete_one(myQuery1)
        flash('Article deleted.', category='danger')
        return redirect(url_for('my_articles'))


# --------------------------------------------------
# Rate Article (Validate)
# --------------------------------------------------


@app.route('/rate/<_id>/<rating>')
@flask_login.login_required
def rate(_id, rating):
    current_user = load_user(flask_login.current_user.get_id())
    Post_to_update = (client[DB_NAME][DB_ARTICLE].find_one(
                      {'_id': ObjectId(_id),
                       'user_postings': {
                           '$elemMatch': {
                               'user_id': ObjectId(current_user._id)}}},
                      {'user_postings': {
                          '$elemMatch': {
                              'user_id': ObjectId(current_user._id)}}}))
    if not(Post_to_update):
        set_user = {'$push': {
            'user_postings': {
                'user_id': ObjectId(current_user._id),
                'good_rating': False,
                'neutral_rating': False,
                'bad_rating': False,
                'comments': ''}}}
        client[DB_NAME][DB_ARTICLE].update_one({
            '_id': ObjectId(_id)}, set_user)
    reset_rating = {'$set': {
        'user_postings.$.good_rating': False,
        'user_postings.$.neutral_rating': False,
        'user_postings.$.bad_rating': False}}
    client[DB_NAME][DB_ARTICLE].update_one({
        '_id': ObjectId(_id),
        'user_postings': {
            '$elemMatch': {
                'user_id': ObjectId(current_user._id)}}},
        reset_rating)
    if rating == 'good':
        set_rating = {'$set': {'user_postings.$.good_rating': True}}
    elif rating == 'neutral':
        set_rating = {'$set': {'user_postings.$.neutral_rating': True}}
    else:
        set_rating = {'$set': {'user_postings.$.bad_rating': True}}
    client[DB_NAME][DB_ARTICLE].update_one({
        '_id': ObjectId(_id),
        'user_postings': {
            '$elemMatch': {
                'user_id': ObjectId(current_user._id)}}},
        set_rating)

    flash('Rating successfully updated. ', category='success')
    return redirect(url_for('show_article', _id=_id))


# --------------------------------------------------
# Commenting Article
# --------------------------------------------------

@app.route('/comment/add/<_id>', methods=['GET', 'POST'])
@flask_login.login_required
def comment(_id):
    current_user = load_user(flask_login.current_user.get_id())
    form = request.form
    if request.method == 'POST':
        input_comments = form.get('input-comments')
    else:
        input_comments = ""
    Post_to_update = (client[DB_NAME][DB_ARTICLE].find_one({
        '_id': ObjectId(_id),
        'user_postings': {
            '$elemMatch': {
                'user_id': ObjectId(current_user._id)}}},
        {'user_postings': {
            '$elemMatch': {
                'user_id': ObjectId(current_user._id)}}}))
    if not(Post_to_update):
        set_user = {'$push': {
            'user_postings': {
                'user_id': ObjectId(current_user._id),
                'good_rating': False,
                'neutral_rating': False,
                'bad_rating': False,
                'comments': ''}}}
        client[DB_NAME][DB_ARTICLE].update_one({
            '_id': ObjectId(_id)}, set_user)
    set_comments = {'$set': {'user_postings.$.comments': input_comments}}
    client[DB_NAME][DB_ARTICLE].update_one({
        '_id': ObjectId(_id),
        'user_postings': {
            '$elemMatch': {
                'user_id': ObjectId(current_user._id)}}},
                set_comments)
    flash('Comments successfully saved. ', category='success')
    return redirect(url_for('show_article', _id=_id))


# --------------------------------------------------
# Displaying comments of an article
# --------------------------------------------------

@app.route('/comment/view/<_id>', methods=['GET', 'POST'])
def view_comment(_id):
    if (id != ""):
        myQuery1 = {'_id': ObjectId(_id)}
        article_data = client[DB_NAME][DB_ARTICLE].find_one(myQuery1)
        if (article_data):
            joint_data = client[DB_NAME][DB_ARTICLE].aggregate([
                {"$match":
                    {'_id': ObjectId(_id)}},
                {"$project":
                    {"_id": 1,
                     "article_title": 1,
                     "user_postings": {"$ifNull": ["$user_postings", []]}}},
                {"$unwind": {
                    "path": "$user_postings",
                    "preserveNullAndEmptyArrays": True}},
                {'$lookup': {
                    'from': "registered_users",
                    'localField': "user_postings.user_id",
                    'foreignField': "_id",
                    'as': "user_details"}},
                {'$project': {
                    'user_postings.user_id': 1,
                    'user_details.nickname': 1,
                    'user_postings.good_rating': 1,
                    'user_postings.neutral_rating': 1,
                    'user_postings.bad_rating': 1,
                    'user_postings.comments': 1}}])
            joint_list = list(joint_data)

        return render_template('/articles/view-comments.template.html',
                               joint_list=joint_list,
                               article_data=article_data,
                               _id=_id)
    else:
        flash('No such article found', category='danger')
        return redirect(url_for('home'))


# --------------------------------------------------
# Cleaning Locations
# --------------------------------------------------
# Allow administrator to manage the list of cleaning location.

@app.route('/cleaning-locations/manage', methods=['GET', 'POST'])
@flask_login.login_required
def manage_cleaning_locations():
    if request.method == 'POST':
        form = request.form
        location_data = client[DB_NAME][DB_LOCATION].find_one(
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
            client[DB_NAME][DB_LOCATION].update_one(
                myquery, updatevalues)
            flash('Location successfully updated', category='success')
            return redirect(url_for("manage_cleaning_locations"))
        # display the record mark for deletion to ask for confirmation
        elif form.get('action') == "delete":
            return render_template("/cleaning-locations/delete.template.html",
                                   location_data=location_data)
        # remove the selected clearning location from the database
        elif form.get('action') == "delete-process":
            myquery = {'_id': ObjectId(form.get('id'))}
            client[DB_NAME][DB_LOCATION].delete_one(myquery)
            flash('Location successfully deleted', category='success')
            return redirect(url_for("manage_cleaning_locations"))
        # Insert the new cleaning location into the database
        elif form.get('action') == "add":
            client[DB_NAME][DB_LOCATION].insert_one(
                {'location': form.get('input-new-location')})
            flash("New cleaning location added.", category='success')
            return redirect(url_for("manage_cleaning_locations"))
        else:
            return redirect(url_for('error_encountered'))
    else:
        # display the add cleaning location form and
        # list out the cleaning locations in the databasse
        location_data = client[DB_NAME][DB_LOCATION].find().sort(
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
        user_data = client[DB_NAME][DB_USER].find_one(
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
                client[DB_NAME][DB_USER].update_one(
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
                    client[DB_NAME][DB_USER].update_one(
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
            client[DB_NAME][DB_USER].delete_one(myquery)
            flash('User successfully deleted', category='success')
            return redirect(url_for("manage_users"))
        else:
            return redirect(url_for('error_encountered'))
    else:
        # display the search box and list out the users in the databasse
        user_data = client[DB_NAME][DB_USER].find().sort(
            'nickname', pymongo.ASCENDING)
        return render_template("/users/manage.template.html",
                               user_data=user_data)


# inbuilt function which handles exception like file not found
@app.errorhandler(404)
def not_found(e):
    flash('File not found.'
          'We will redirect you to the home page in a moment.',
          category='success')
    return redirect(url_for("home"))


@app.route('/error-encountered')
def error_encountered():
    return render_template('/error-encountered.template.html')


# flask boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
