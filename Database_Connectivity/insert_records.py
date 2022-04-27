# inserting records into table.

import dbconnect
from dbconnect import connection, cur
from mysql.connector import Error


def insert_records(query, val):
    try:
        cur.executemany(query, val)
        connection.commit()
        print(cur.rowcount, " was added to student table")
        connection.close()
    except Error as e:
        print(f"Error {e} occured.")


query = """
INSERT INTO student (student_id, student_name, course_name, marks) values (%s, %s, %s, %s)
"""

val = [
    (11, 'Ajay', 'Python', 89),
    (13, 'Bharath', 'Java', 97),
    (14, 'Chethan', 'C++', 90),
    (18, 'Kumar', 'Python', 92)
]

insert_records(query, val)
