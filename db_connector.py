import pymysql
from pypika import Query, Table, Field


# function for creating a new user into the DB:
def add_user(user_id, user_name, creation_date):
    schema_name = "freedb_MySql1"
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_yfatzabusky', passwd='&ApvZjGPcN*#G5A',
                           db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Inserting data into table
    cursor.execute(
        f"INSERT into {schema_name}.new_users (user_id, user_name, creation_date) VALUES ('{user_id}', '{user_name}', '{creation_date}')")

    cursor.close()
    conn.close()


# function for updating an existing user into the DB:
def update_user(user_id, user_name):
    schema_name = "freedb_MySql1"
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_yfatzabusky', passwd='&ApvZjGPcN*#G5A',
                           db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Updating data inside the table
    cursor.execute(f"UPDATE {schema_name}.new_users SET user_name = '{user_name}' WHERE user_id = {user_id}")

    cursor.close()
    conn.close()


# function for deleting an existing user into the DB:
def delete_user(user_id):
    schema_name = "freedb_MySql1"
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_yfatzabusky', passwd='&ApvZjGPcN*#G5A',
                           db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Deleting data from table
    cursor.execute(f"DELETE FROM {schema_name}.new_users WHERE user_id = {user_id}")

    cursor.close()
    conn.close()


# function for checking if a user does really exist in the DB using the Primary Key - user_id:
def value_exists(user_id):
    schema_name = "freedb_MySql1"
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_yfatzabusky', passwd='&ApvZjGPcN*#G5A',
                           db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()


    # Execute a SELECT statement
    cursor.execute(f"SELECT  * FROM {schema_name}.new_users WHERE user_id =%s", (user_id,))

    # Fetch the rows
    rows = cursor.fetchall()
    # If there are any rows, the value exists in the database and will return True
    if rows:
        return True
    else:
        return False

    cursor.close()
    conn.close()


# function for getting the user_name using a user_id:
def get_user_name_from_db(user_id):
    schema_name = "freedb_MySql1"
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_yfatzabusky',
                           passwd='&ApvZjGPcN*#G5A',
                           db=schema_name)
    conn.autocommit(True)
    # Getting a cursor from Database
    cursor = conn.cursor()

    if value_exists(user_id):
        # Selecting data where the user_id is like chosen:
        cursor.execute(f"SELECT * FROM {schema_name}.new_users WHERE user_id = {user_id};")

        # Get the user_name value into a parameter:
        for row in cursor:
            user_name = (row[1])

        cursor.close()
        conn.close()

        return user_name
    else:
        return None


# function that prints all the data inside the user table:
def print_users_table():
    schema_name = "freedb_MySql1"
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_yfatzabusky',
                           passwd='&ApvZjGPcN*#G5A',
                           db=schema_name)
    conn.autocommit(True)
    # Getting a cursor from Database
    cursor = conn.cursor()
    # Selecting data where the user_id is like chosen:
    cursor.execute(f"SELECT * FROM {schema_name}.new_users ")
    # Fetch the rows
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    cursor.close()
    conn.close()


# function that prints a selected user data from the user table:
def select_user_from_table(user_id):
    schema_name = "freedb_MySql1"
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_yfatzabusky',
                           passwd='&ApvZjGPcN*#G5A',
                           db=schema_name)
    conn.autocommit(True)
    # Getting a cursor from Database
    cursor = conn.cursor()
    # Selecting data where the user_id is like chosen:
    cursor.execute(f"SELECT * FROM {schema_name}.new_users WHERE user_id = {user_id} ")
    # Fetch the rows
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
