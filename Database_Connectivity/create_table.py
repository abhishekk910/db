# creating table

import dbconnect
from mysql.connector import Error

from dbconnect import connection, cur


def create_table(query):
    try:
        cur.execute(query)
        connection.close()
    except Error as e:
        print(e)


query = """
create table student (student_id INT PRIMARY KEY, student_name VARCHAR(20), 
course_name VARCHAR(20), marks INT)
"""
create_table(query)
