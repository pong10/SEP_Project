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
        if(self.user[0:3]=='Ad_' or self.user=='pnmoiannnygcoeu362'):# if admin
            self.mycursor.execute("SELECT Username,Password from Admin")
        else:
            self.mycursor.execute("SELECT Username,Password from Customer")
        myresult=self.mycursor.fetchall()
        for i,j in myresult:
            if self.user==i and self.password==j:
                return True
        return False

a=SignIn('pnmoiannnygcoeu362','qwerty')
print(a.SignIn())