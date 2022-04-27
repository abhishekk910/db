# deleting records from table.

import dbconnect
from dbconnect import connection, cur
from mysql.connector import Error


def create_table(query):
    try:
        cur.execute(query)
        connection.commit()
        print(cur.rowcount, "record(s) deleted")
        connection.close()
    except Error as e:
        print(f"Error {e} occured.")


query = "DELETE FROM student where student_id = 13"
create_table(query)
