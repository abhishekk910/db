# updating the records in table.

import dbconnect
from dbconnect import connection, cur
from mysql.connector import Error


def create_table(query):
    try:
        cur.execute(query)
        connection.commit()
        print(cur.rowcount, "record(s) affected")
        connection.close()

    except Error as e:
        print(f"Error {e} occured.")


query = "update student set marks = 99 where student_id = 13"
create_table(query)
