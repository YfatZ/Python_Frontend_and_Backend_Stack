import time
import flask
import pymysql
import requests

import os
import signal

from flask import Flask, request

# import all relevant functions from another method :
from db_connector import get_user_name_from_db

app = Flask(__name__)


# function for getting a user_name and printing it to the browser
@app.route('/new_users/get_user_name/<user_id>')
def get_user_name(user_id):
    # Use a function to get the_user name of a given user id stored inside users table
    user_name = get_user_name_from_db(user_id)

    # check if the user_name didn't return a value, then return an error
    if user_name is None:
        return "<H1 id='error'>" "no such user: " + user_id + "</H1>"
    # in case it did return a value, return the value of the user_name
    else:
        return "<H1 id='user'>" + user_name + "</H1>"

# In order to add automatic termination to the web application server
@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


# run the app:
app.run(host='127.0.0.1', debug=True, port=5001)



