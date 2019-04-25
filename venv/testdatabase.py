import mysql.connector
class SignUp():
    mydb = mysql.connector.connect(
        host="35.198.233.244",
        user="root",
        passwd="123456",
        database="parcelexpress",
        port="3306"
    )
    mycursor = mydb.cursor()
    user = ''
    password = ''

    def __init__(self, user, password):
        self.user = user
        self.password = password
    def UserExist(self):
        self.mycursor.execute("SELECT Username FROM Customer")
        myresult=self.mycursor.fetchall()
        print(myresult)
        if self.user in myresult:
          return False
        else:
          return True
    def signUp(self):
        if(self.UserExist()==True):
          sql = "INSERT INTO Customer(Username,Password) VALUES (%s, %s)"
          val = (self.user, self.password)
          self.mycursor.execute(sql, val)
          self.mydb.commit()
        else:
          raise InValid('User is already exist')

    def print(self):
        self.mycursor.execute("SELECT Username, Password FROM Customer")
        myresult = self.mycursor.fetchall()

        for x in myresult:
            print(x)
a=SignUp('manyou','123456')
a.signUp()
a.print()

# mycursor.execute("SELECT Username, Password FROM Customer")
# myresult = mycursor.fetchall()
#
# for x in myresult:
#  print(x)
# sql = "INSERT INTO Customer(Username,Password) VALUES (%s, %s)"
# val = ("Somphon", "123456")
# mycursor.execute(sql, val)
# mydb.commit()
# print("1 record inserted, UserId:", mycursor.lastrowid)
# mycursor.execute("CREATE TABLE Customer (UserId INT AUTO_INCREMENT PRIMARY KEY,Username VARCHAR(20),Password VARCHAR (20))")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#  print(x)
# mycursor=mydb.cursor()
# mycursor.execute("CREATE TABLE User(Username VARCHAR(255),Password VARCHAR(255),
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#    print(x)
