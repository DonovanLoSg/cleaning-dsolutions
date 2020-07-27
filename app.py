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

# START WRITING YOUR CODE


@app.route('/')
def index():
    return '<h1>Home</h1>'


@app.route('/login')
def login():
    return '<h1>Login</h1>'


@app.route('/logout')
def logout():
    return '<h1>Logout</h1>'


@app.route('/register')
def register():
    return '<h1>Register</h1>'


@app.route('/my-profile')
def my_profile():
    return '<h1>My Profile</h1>'


@app.route('/about')
def about():
    return '<h1>About</h1>'


@app.route('/instructions')
def instructions():
    return '<h1>Instructions</h1>'


@app.route('/list-articles')
def list_articles():
    return '<h1>Articles</h1>'


@app.route('/my-articles')
def my_articles():
    return '<h1>My Articles</h1>'


@app.route('/contribute-articles')
def contribute_articles():
    return '<h1>Contribute Articles</h1>'


@app.route('/manage-cleaning-locations')
def manage_cleaning_locations():
    return '<h1>Cleaning Locations</h1>'


@app.route('/manage-users')
def manage_users():
    return '<h1>Users</h1>'


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
