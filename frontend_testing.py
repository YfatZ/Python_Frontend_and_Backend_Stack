import selenium
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Start a Selenium Webdriver session
driver = webdriver.Chrome(service=Service("C:\\Users\\Owner\\Downloads\\chromedriver.exe"))

driver.implicitly_wait(5)


# choose user_id to check:
user_id = 5


try:
    # Navigate to web interface URL using an existing user id (user_id=1)
    myUrl = "http://127.0.0.1:5001/new_users/get_user_name/" + str(user_id)
    driver.get(myUrl)
    # Check that the user_name element is showing (web element exists)
    if driver.find_element(By.ID, value='user'):
        # If it shows - print user_name (using the ID locator)
        user_name = driver.find_element(By.ID, value='user')
        print(user_name.text)
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