import pymysql
import json
from flask import Flask
import time

import requests

# import all relevant functions from another method :
from db_connector import print_users_table, select_user_from_table, value_exists

# choose user_id to check:
user_id = 1

# choose user_name and creation_date for the new user:
user_name = "john"
creation_date = "03/01/2023"

try:
    # first check if the user_id exists:
    if not value_exists(user_id):
        # Navigate to URL using the user_id:
        backend_url = "http://127.0.0.1:5000/new_users/" + str(user_id)
        # Post a new user data to the REST API using POST method:
        res = requests.post(backend_url, json={"user_name": user_name, "creation_date": creation_date})
        print(res.text)
        post_user_name = res.json()['user_added']

        # print only for separation of the printing:
        print("______________")

        # Submit a GET request
        res = requests.get(backend_url)
        print(res.text)
        get_user_name = res.json()['user_name']

        # print only for separation of the printing:
        print("______________")

        # make sure status code is 200 and data equals to the posted data:
        # check if the status is 200 (ok):
        if res.json()['status']:
            print("status code is ok (200)")
            # compare between post_user_name and get_user_name:
            if post_user_name == get_user_name:
                print("The data is equal, user_name is correct")
            else:
                print("data is unequal, user name is not the same.")
        else:
            print("status code is not ok (not 200)")

        # print only for separation of the printing:
        print("______________")

        # print all data on the new_users table:
        print_users_table()

        # print only for separation of the printing:
        print("______________")

        # to make sure the user_id stored the correct user_name
        # select only the requested user data from the table using user_id:
        select_user_from_table(user_id)
    else:
        # Any failure will throw an exception using the following code: raise Exception("test failed")
        raise Exception("test failed")

except:
    # Any failure will throw an exception using the following code: raise Exception("test failed")
    raise Exception("test failed")
