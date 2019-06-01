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

    def __init__(self, user, password,firstname,lastname,phonenumber,email,province):
        self.user = user
        self.password = password
        self.firstname=firstname
        self.lastname=lastname
        self.phoneNumber=phonenumber
        self.email=email
        self.province=province

    def insertDatabaseUser(self):

        userName=self.firstname+" "+self.lastname
        command="insert into Users(Name,username,password,PhoneNumber, Email,Province)values(%s,%s,%s,%s,%s,%s)"
        self.mycursor.execute(command,(userName,self.user,self.password,self.phoneNumber,self.email,self.province))
        self.mydb.commit()

    def insertDatabaseAdmin(self):

        userName=self.firstname+" "+self.lastname
        command="insert into Admin(Name,username,password,PhoneNumber, Email,Province)values(%s,%s,%s,%s,%s,%s)"
        self.mycursor.execute(command,(userName,self.user,self.password,self.phoneNumber,self.email,self.province))
        self.mydb.commit()

    def insertDatabaseDriver(self):

        userName=self.firstname+" "+self.lastname
        command="insert into Driver(Name,username,password,PhoneNumber, Email,Province)values(%s,%s,%s,%s,%s,%s)"
        self.mycursor.execute(command,(userName,self.user,self.password,self.phoneNumber,self.email,self.province))
        self.mydb.commit()

    def UserExist(self):
        if(self.user[0:3]=='Ad_'):# if admin
            self.mycursor.execute("SELECT username FROM Admin")
        elif(self.user[0:3]=='Dr_'):
            self.mycursor.execute("SELECT username FROM Driver")
        else:
            self.mycursor.execute("SELECT username FROM Users")
        myresult=self.mycursor.fetchall()
        DataUser=[x[0] for x in myresult]

        for i in DataUser:
            if(self.user in i):
                return True
        return False

    def signUp(self):
        if(self.UserExist()==False and self.user[0:3]=='Ad_'):
            self.insertDatabaseAdmin()
        elif(self.UserExist()==False and self.user[0:3]=='Dr_'):
            self.insertDatabaseDriver()
        elif (self.UserExist() == False and self.user[0:3] != 'Ad_' and self.user[0:3] != 'Dr_'):
            self.insertDatabaseUser()
        else:
            raise InValid('User is already exist')

    def print(self):
        self.mycursor.execute("SELECT Username, Password FROM Customers")
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)

t=SignUp('Usesdfdsaf','sdafsdfsdf','Somphon','Reufds','02455666','manza1921@hiotaert','asdsad')
t.signUp()
