from flask import Flask, render_template, request, redirect, url_for, flash
import pymongo
from dotenv import load_dotenv
from bson import ObjectId
import os
import datetime
import flask_login
# from passlib.hash import pbkdf2_sha256


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
app.secret_key = SESSION_KEY

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
def user_loader(email):
    # find the user from the database by its email
    user_data = client[DB_NAME][USER_COLLECTION_NAME].find_one({
        'email': email
    })
    print(user_data)
    if user_data:
        # create a new user object
        current_user = User()
        current_user.id = user_data['email']
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


# Get up to 5 articles from the database
#   and display it on the homepage,
#   allow user to click on one of these 5 default article titles
#   to view the article.
# Display a search panel to allow users to search
#  using different methods: search by article titles,
# search by cleaning location or search by tags.
# When a search is executed, it will return the result
# in a list containing article titles and cleaning locations.
# Include an option to display all the articles.
# Display a search panel to allow administrator to search
# using different methods: search by article titles,
# search by cleaning location or search by tags.
@app.route('/')
def index():
    return redirect(url_for("home"))


@app.route('/home')
def home():
    return render_template("home.template.html")

# Allow members and administrators to log in
# through a login page accepting nickname and password.
# If the validation is successful,
# redirect the user to administrators’ access area
# if they are administrators,
# else they will be redirected to a members’ access area.
# If the validation is unsuccessful,
# they will be alerted with a message and allowed to retry again.
#


@app.route('/auth/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':  # recieved as form submitted
        return render_template("/auth/login_process.template.html")
    else:
        # This template shows a login form, only called if the request.method was not 'POST'.
        return render_template("/auth/login.template.html")

    #     email = request.form['email']
    #     password = request.form['password']
    #     try:
    #         # Check if the user is valid, this would go through a database.
    #         if User.is_login_valid(email, password):
    #             session['email'] = email
    #             # When we redirect them, we already have data saved in the session
    #             return '<h1>Login</h1>'
    #     except Exception as e:
    #         # Send user to an error page if something happened during login.
    #         return '<h1>Login Error</h1>'


@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return render_template("/unauthorized.template.html")


# A instruction to log the user out and return to the home page
@app.route('/auth/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('home'))

# Include a link to the user registration page which accept
# nickname, email address, password and password retype.
# The email address must be valid and unique in the system,
# the password must be at least eight characters and contain
# at least one letter and one number, the password retype
# must be same as the password.


@app.route('/auth/register')
def register():
    return render_template("/auth/register.template.html")


# Allow member to view their own profile comprising of
# nickname, email address and password.
# Allow member to update their nickname
# or reset their password.
# Allow administrator to view their own profile
# comprising of nickname, email address and password.
# Allow administrator to update their nickname
# or reset their password.
@app.route('/users/my-profile')
@flask_login.login_required
def my_profile():
    return render_template("/user/my-profile.template.html")


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
@app.route('/articles/show/<id>')
def show_article(id):
    return render_template("/articles/article.template.html", id=id)


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
    return render_template("/articles/my-list.template.html")

# Include an article creation page accepting article titles,
# cleaning location, article content, cleaning items,
# cleaning supplies and tags.
# Include an article creation page accepting article titles,
#  cleaning location, article content, cleaning items, cleaning supplies and tags.


@app.route('/articles/contribute')
@flask_login.login_required
def contribute_articles():
    return render_template("/articles/contribute.template.html")


# Allow administrator to manage the list of cleaning location.
@app.route('/cleaning-locations/manage')
@flask_login.login_required
def manage_cleaning_locations():
    return render_template("/cleaning-locations/manage.template.html")


# Display a list of all the users.
# Allow administrator to search for a user.
# Display the selected user profile.
# Allow administrator to edit the user profile (modify nickname).
# Allow administrator to delete user profile.
# Allow administrator to reset user password.
# Allow administrator to assign admin rights.
@app.route('/users/manage')
@flask_login.login_required
def manage_users():
    return render_template("/users/manage.template.html")


# inbuilt function which handles exception like file not found
@app.errorhandler(404)
def not_found(e):
    return render_template('/file-not-found.template.html')


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
