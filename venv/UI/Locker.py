import mysql.connector
class Locker():
    mydb = mysql.connector.connect(
        host="35.198.233.244",
        user="root",
        passwd="123456",
        database="parcelexpress",
        port="3306"
    )
    mycursor = mydb.cursor()
    def __init__(self,Tracking,UserName):
        self.trackingNumber=Tracking
        self.Name=UserName
    def open(self):
        self.mycursor.execute("select TrackingNumber,Sender from Parcel")
        TrackingNumber_Username=self.mycursor.fetchall()
        for i,j in TrackingNumber_Username:
            if(self.trackingNumber==i and self.Name==j):
                return True
        return False


