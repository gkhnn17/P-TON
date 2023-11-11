import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost", #192.23.45.56
    user = "root",
    password = "Mysql123",
    database = "mydatabase"



)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers(name VARCHAR(255),address VARCHAR(255))")
#mycursor.execute("CREATE DATABASE mydatabase")
#mycursor.execute("SHOW DATABASES")
"""
for x in mycursor:
    print(x)"""

print(mydb)