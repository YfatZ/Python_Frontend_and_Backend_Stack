import pymysql

# Method for creating a table inside the Database:

schema_name = "freedb_MySql1"

# Establishing a connection to DB
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_yfatzabusky', passwd='&ApvZjGPcN*#G5A', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
statementToExecute = "CREATE TABLE `freedb_MySql1`.`new_users` (`user_id` INT NOT NULL,`user_name` VARCHAR(50) NOT NULL,`creation_date` VARCHAR(50) NOT NULL,PRIMARY KEY (`user_id`));"
cursor.execute(statementToExecute)


cursor.close()
conn.close()
