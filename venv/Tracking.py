import mysql.connector
class Tracking():
    state_of_parcel = ['Parcel is in the source branch', 'Parcel Express driver prepare to deliver',
                       'Parcel is at its destination', 'Waiting for receiver', 'Parcel receive']
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
    def __init__(self,TrackingNumber,name):
        self.TrackingNumber=TrackingNumber
        self.name=name
    def Tracking(self):
        State_information=''
        User_information=''
        self.mycursor.execute("select TrackingNumber,UserID from Tracking_ID;")
        myresult=self.mycursor.fetchall()
        for i,j in myresult:
            if self.TrackingNumber==i and self.UserID==j:
                State_information=self.mycursor.execute(("select State from Parcel where TrackingNumber ='%s'"),i)
                User_information=self.mycursor.execute(("select * from User where UserID='%s'"),j)


