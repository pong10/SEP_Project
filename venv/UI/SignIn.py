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

    def SignIn(self):
        if(self.user[0:3]=='Ad_'):# if admin
            self.mycursor.execute("SELECT username,Password from Admin")
        elif(self.user[0:3]=='Dr_'):
            self.mycursor.execute("SELECT username,Password from Driver")
        elif(self.user=='pnmoiannnygcoeu362'):
            self.mycursor.execute("SELECT username,Password from Master")
        else:
            self.mycursor.execute("SELECT username,Password from Users")
        myresult=self.mycursor.fetchall()
        for i,j in myresult:
            if self.user==i and self.password==j:
                return True
        return False
