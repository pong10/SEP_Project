from Employee import *
import mysql.connector
import uuid
class Admin(Employee):
    mydb = mysql.connector.connect(
        host="35.198.233.244",
        user="root",
        passwd="123456",
        database="parcelexpress",
        port="3306"
    )
    mycursor = mydb.cursor()
    def __init__(self, name, address, phone, email):
        super().__init__(name,address,phone,email)

    def generate(self,countrycode='--'):
        front = 'ABC'
        body = uuid.uuid4().hex
        body = body.upper()[0:8]
        code = front + body + countrycode
        return code

    def createTrackingNumber(self,name):
        tracking_id=  self.generate('TH')
        sql = "INSERT INTO Tracking_ID(ID,NameOfUser) VALUES (%s, %s)"
        val = (tracking_id,name)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def Tracking(self,TrackingId,name):
        self.mycursor.execute("select ID,NameOfUser from Tracking_ID;")
        myresult=self.mycursor.fetchall()
        for i,j in myresult:
            if TrackingId==i and name==j:
                return True
        return False

t=Admin("somphon","123456",'0922795229','manza1921@hotmail.com')
print(t.generate('TH'))



