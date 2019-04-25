import mysql.connector

mydb = mysql.connector.connect(
  host="35.198.233.244",
  user="root",
  passwd="123456",
  database="parcelexpress",
  port="3306"
)
query =db.cursor()
#mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE User(Username VARCHAR(255),Password VARCHAR(255),
#mycursor.execute("SHOW DATABASES")
#for x in mycursor:
#    print(x)