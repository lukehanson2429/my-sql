import os
import datetime
import pymysql


# Get username from Cloud9 workspace
# (modify this variable if running on another enviroment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try: 
    #Run A query
    with connection.cursor() as cursor:
        rows = cursor.executemany("DELETE FROM Friends WHERE name in ('jim, 'bob')")
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()