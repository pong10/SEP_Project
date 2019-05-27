import mysql.connector
class SignIn():
    mydb = mysql.connector.connect(
        host="35.198.233.244",
        user="root",
        passwd="123456",
        database="parcelexpress",
        port="3306"
    )
    mycursor = mydb.cursor()

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def UserExist(self):
        self.mycursor.execute("SELECT  Username FROM Customer")
        myresult=self.mycursor.fetchall()
        t = self.binarySearch(myresult,0,len(myresult),self.user)
        if t == True:
            return True
        else:
            return False

    def SignIn(self):
        self.mycursor.execute("SELECT Username,Password from Customer")
        myresult=self.mycursor.fetchall()
        for i,j in myresult:
            if self.user==i and self.password==j:
                return True
        return False
a=SignIn('Pong','123456')
print(a.SignIn())