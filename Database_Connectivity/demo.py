import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="abhi",
    passwd="Root@1312",
)

print(conn)

