import pymysql
import json
from flask import Flask
import time
import requests

import selenium
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from db_connector import print_users_table, select_user_from_table, value_exists

# choose user_id to check:
user_id = 9

# choose user_name and creation_date for the new user:
user_name = "Alona"
creation_date = "05/01/2023"

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

        # select only the requested user data from the table using user_id:
        select_user_from_table(user_id)
    else:
        # Any failure will throw an exception using the following code: raise Exception("test failed")
        raise Exception("test failed")

except:
    # Any failure will throw an exception using the following code: raise Exception("test failed")
    raise Exception("test failed")

# Start a Selenium Webdriver session
driver = webdriver.Chrome(service=Service("C:\\Users\\Owner\\Downloads\\chromedriver.exe"))
driver.implicitly_wait(5)

try:
    # Navigate to web interface URL using an existing user id
    frontend_url = "http://127.0.0.1:5001/new_users/get_user_name/" + str(user_id)
    driver.get(frontend_url)
    # Check that the user_name element is showing (web element exists)
    if driver.find_element(By.ID, value='user'):
        # If it shows - print user_name (using the ID locator)
        user_name = driver.find_element(By.ID, value='user')
        print(user_name.text)
        # print only for separation of the printing:
        print("______________")
        # Check that the user_name is correct:
        if user_name.text == get_user_name == post_user_name:
            print("GOOD! The user_name is the same as GET and POST user_name values")
        else:
            print("BAD! The user_name is not the same as GET and POST user_name values")

    elif driver.find_element(By.ID, value='error'):
        # If it doesn't show - print error (using the ID locator)
        no_such_user = driver.find_element(By.ID, value='error')
        print(no_such_user.text)
    else:
        print('No element found')

except:
    # Any failure will throw an exception using the following code: raise Exception("test failed")
    raise Exception("test failed")

time.sleep(10)