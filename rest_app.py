import flask
import requests

import os
import signal

import pymysql
from flask import Flask, request, render_template


# import all relevant functions from another method :
from db_connector import add_user, update_user, delete_user, value_exists

app = Flask(__name__)


# function for requested methods: 'GET', 'POST', 'PUT', 'DELETE'
@app.route('/new_users/<user_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user(user_id):
    # Get request method:
    # returns the user_name stored in the database for a given user id
    if request.method == 'GET':
        # first check if the user_id exists:
        if value_exists(user_id):
            schema_name = "freedb_MySql1"
            # Establishing a connection to DB
            conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_yfatzabusky',
                                   passwd='&ApvZjGPcN*#G5A',
                                   db=schema_name)
            conn.autocommit(True)
            # Getting a cursor from Database
            cursor = conn.cursor()

            # Selecting data where the user_id is like chosen:
            cursor.execute(f"SELECT * FROM {schema_name}.new_users WHERE user_id = {user_id};")
            # Get the user_name value into a parameter:
            for row in cursor:
                user_name = (row[1])

            cursor.close()
            conn.close()

        # returns the information:
            # On success:
            return {'status': 'Ok', 'user id': user_id, 'user_name': user_name}, 200  # status code
        else:
            # On error:
            return {'status': 'Error', 'reason': 'no such id'}, 500 # status code

    # POST request method:
    # Creating a new user into the Database with the id passed in the URL and with user_name passed in the request payload
    if request.method == 'POST':
        try:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            creation_date = request_data.get('creation_date')
            # using add_user def for inserting data into the DB
            add_user(user_id, user_name, creation_date)

            # first check if the user_id exists and then returns the information:
            if value_exists(user_id):
                # On success:
                return {'status': 'Ok', 'user_added': user_name}, 200  # status code
            else:
                # On error:
                return {'status': 'Error', 'reason': 'id already exists'}, 500 # status code
        except pymysql.err.IntegrityError as error:
            # On error:
            return {'status': 'Error', 'reason': 'id already exists'}, 500 # status code

    # PUT request method:
    # modifying existing user_name in the database
    if request.method == 'PUT':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        # using add_user def for inserting data into the DB
        update_user(user_id, user_name)

        # first check if the user_id exists and then returns the information:
        if value_exists(user_id):
            # On success:
            return {'status': 'ok', 'user_updated': user_name}, 200  # status code
        else:
            # On error:
            return {'status': 'Error', 'reason': 'no such id'}, 500 # status code

    # DELETE request method:
    # deleting existing user from database
    if request.method == 'DELETE':
        try:
            # first check if the user_id exists and then delete the user
            if value_exists(user_id):
                delete_user(user_id)

            # returns the information:
                # On success:
                return {'status': 'ok', 'user_deleted': user_id}, 200  # status code
            else:
                # On error:
                return {'status': 'Error', 'reason': 'no such id'}, 500 # status code
        except TypeError as error:
            # On error:
            return {'status': 'Error', 'reason': 'no such id'}, 500 # status code

# In order to add automatic termination to the REST Api server
@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'

# Route error handler for non-existing routes - 404
@app.errorhandler(404)
def page_not_found(e):
    return "<title>Page Not Found</title> <h1>Page Not Found - Error 404</h1> <p> Oops! Looks like the page doesn't exist </p>", 404  # status code


# run the app:
app.run(host='127.0.0.1', debug=True, port=5000)



