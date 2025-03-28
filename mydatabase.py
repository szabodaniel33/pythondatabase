import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql"
)

mycursor = mydb.cursor()

DATABASE= "my_database"
mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")

mycursor.execute("SHOW DATABASES")

for x in  mycursor:
    print(x)

mycursor.execute(f"USE {DATABASE}")