# fetching records from table

import dbconnect
from dbconnect import connection, cur
from mysql.connector import Error

def select_records(query):
    try:
        cur.execute(query)
        result = cur.fetchall()
        for i in result:
            print(i)

    except Error as e:
        print(f"Error {e} occured")


query = """
select * from student
"""

select_records(query)