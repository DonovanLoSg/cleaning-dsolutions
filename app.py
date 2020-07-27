from flask import Flask, render_template, request, redirect, url_for, flash
import pymongo
from dotenv import load_dotenv
from bson import ObjectId
import os
import datetime

# load in the variables in the .env file into our operating system environment
load_dotenv()

app = Flask(__name__)

# connect to mongo
MONGO_URI = os.environ.get('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)

# define my db_name
DB_NAME = os.environ.get('DB_NAME')

# read in the SESSION_KEY variable from the operating system environment
SESSION_KEY = os.environ.get('SESSION_KEY')

# set the session key
app.secret_key = SESSION_KEY

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
    return '<h1>Home</h1>'


# Allow members and administrators to log in
# through a login page accepting nickname and password.
# If the validation is successful,
# redirect the user to administrators’ access area
# if they are administrators,
# else they will be redirected to a members’ access area.
# If the validation is unsuccessful,
# they will be alerted with a message and allowed to retry again.
@app.route('/login')
def login():
    return '<h1>Login</h1>'


# A instruction to log the user out and return to the home page
@app.route('/logout')
def logout():
    return '<h1>Logout</h1>'


# Include a link to the user registration page which accept
# nickname, email address, password and password retype.
# The email address must be valid and unique in the system,
# the password must be at least eight characters and contain
# at least one letter and one number, the password retype
# must be same as the password.
@app.route('/register')
def register():
    return '<h1>Register</h1>'


# Allow member to view their own profile comprising of 
# nickname, email address and password.
# Allow member to update their nickname 
# or reset their password.
# Allow administrator to view their own profile 
# comprising of nickname, email address and password.
# Allow administrator to update their nickname 
# or reset their password.
@app.route('/my-profile')
def my_profile():
    return '<h1>My Profile</h1>'


@app.route('/about')
def about():
    return '<h1>About</h1>'


@app.route('/instructions')
def instructions():
    return '<h1>Instructions</h1>'


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
@app.route('/list-articles')
def list_articles():
    return '<h1>Articles</h1>'


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
@app.route('/show-article')
def show_article():
    return '<h1>Article #</h1>'


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
@app.route('/my-articles')
def my_articles():
    return '<h1>My Articles</h1>'

# Include an article creation page accepting article titles, 
# cleaning location, article content, cleaning items, 
# cleaning supplies and tags.
# Include an article creation page accepting article titles,
#  cleaning location, article content, cleaning items, cleaning supplies and tags.
@app.route('/contribute-articles')
def contribute_articles():
    return '<h1>Contribute Articles</h1>'


# Allow administrator to manage the list of cleaning location.
@app.route('/manage-cleaning-locations')
def manage_cleaning_locations():
    return '<h1>Cleaning Locations</h1>'


# Display a list of all the users.
# Allow administrator to search for a user.
# Display the selected user profile.
# Allow administrator to edit the user profile (modify nickname).
# Allow administrator to delete user profile.
# Allow administrator to reset user password.
# Allow administrator to assign admin rights.
@app.route('/manage-users')
def manage_users():
    return '<h1>Users</h1>'


# inbuilt function which handles exception like file not found
@app.errorhandler(404)
def not_found(e):
    return '<h1>File Not Found </h1>'


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
