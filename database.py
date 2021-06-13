import mysql.connector

class Mydbconnection:

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sa",
    database="mydatabase"
    )
