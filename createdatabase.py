import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sa",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
mycursor.execute("CREATE TABLE IF NOT EXISTS student (name VARCHAR(255), email VARCHAR(255))")

sql = "INSERT INTO student (name, email) VALUES (%s, %s)"
val = ("neha", "neha@gmail.com")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.close
mydb.close
