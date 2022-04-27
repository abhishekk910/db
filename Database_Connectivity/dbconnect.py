import mysql.connector

from mysql.connector import Error


def mydbConnection(hostname, user_name, user_password, db):
    try:
        conn = mysql.connector.connect(
            host=hostname,
            user=user_name,
            passwd=user_password,
            database=db
        )
        # print(conn)
        # print("Connection to MySQL DB successful")

    except Error as e:
        print(f"The error '{e}' occurred")

    return conn


connection = mydbConnection("localhost", "abhi", "Root@1312", "PythonDB")
cur = connection.cursor()
