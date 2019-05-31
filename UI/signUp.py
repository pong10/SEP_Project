'''
import mysql.connector
class InValid(Exception): pass
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
        if(self.user[0:3]=='Ad_'):# if admin
            self.mycursor.execute("SELECT  Username FROM Admin")
        else:
            self.mycursor.execute("SELECT  Username FROM Customers")
        myresult=self.mycursor.fetchall()
        DataUser=[x[0] for x in myresult]
        #print("Datauser: ",DataUser)
        for i in DataUser:
            if(self.user == i):
                return True
        return False

    def signUp(self):
        if(self.UserExist()==False and self.user[0:3]=='Ad_'):
            sql = "INSERT INTO Admin(Username,Password) VALUES (%s, %s)"
            val = (self.user, self.password)
            self.mycursor.execute(sql, val)
            self.mydb.commit()
        elif(self.UserExist()==False and self.user[0:3]!='Ad_'):
            sql = "INSERT INTO Customers(Username,Password) VALUES (%s, %s)"
            val = (self.user, self.password)
            self.mycursor.execute(sql, val)
            self.mydb.commit()
        else:
            raise InValid('User is already exist')

    def print(self):
        self.mycursor.execute("SELECT Username, Password FROM Customers")
        myresult = self.mycursor.fetchall()

        for x in myresult:
            print(x)
#a=SignUp('Ad_pong','123456')
#a.signUp()
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
'''
import mysql.connector
import uuid
class InValid(Exception): pass
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

    def UserIdCreation(self):
        front = '000'
        body = uuid.uuid4().int
        body=body%10000000
        code = front+str(body)
        return code
    def insert(self,uid,phn,ema,fn,pv):
        self.mycursor.execute("INSERT INTO User(UserId,PhoneNumber,Email,Firstname,Province) values(%d,%s,%s,%s,%s)"%(uid,phn,ema,fn,pv))
    def UserExist(self):
        if(self.user[0:3]=='Ad_'):# if admin
            self.mycursor.execute("SELECT  Username FROM Admin")
        else:
            self.mycursor.execute("SELECT  Username FROM Customers")
        myresult=self.mycursor.fetchall()
        DataUser=[x[0] for x in myresult]
        print(DataUser)
        for i in DataUser:
            print(i)
            print(self.user)
            if(self.user in i):
                return True
        return False

    def signUp(self):
        if(self.UserExist()==False and self.user[0:3]=='Ad_'):
            sql = "INSERT INTO Admin(Username,Password) VALUES (%s, %s)"
            val = (self.user, self.password)
            self.mycursor.execute(sql, val)
            self.mydb.commit()
        elif(self.UserExist()==False and self.user[0:3]!='Ad_'):
            sql = "INSERT INTO Customers(Username,Password) VALUES (%s, %s)"
            val = (self.user, self.password)
            self.mycursor.execute(sql, val)
            self.mydb.commit()
        else:
            raise InValid('User is already exist')

    def print(self):
        self.mycursor.execute("SELECT Username, Password FROM Customers")
        myresult = self.mycursor.fetchall()

        for x in myresult:
            print(x)
#a=SignUp('Ad_pong','123456')
#print(a.UserIdCreation())
