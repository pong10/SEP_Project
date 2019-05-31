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

    def __init__(self,TrackingNumber,Sender):
        self.TrackingNumber=TrackingNumber
        self.information=''
        self.UserID=Sender

    def trackPercent(self,state):
        i=20
        for i in range(0,5):
            if(self.state_of_parcel[i]==state):
                return i+20

    def getTrackingNumber(self):
        return self.information[0][0]

    def getSender(self):
        return self.information[0][1]

    def getSender_postcode(self):
        return self.information[0][2]

    def getSender_address(self):
        return self.information[0][3]

    def getSender_province(self):
        return self.information[0][4]

    def getSender_contact(self):
        return self.information[0][5]

    def getReceiver(self):
        return self.information[0][6]

    def getReceiver_address(self):
        return self.information[0][7]

    def getReceiver_province(self):
        return self.information[0][8]

    def getReceiver_postcode(self):
        return self.information[0][9]

    def getReceiver_contact(self):
        return self.information[0][10]

    def getState(self):
        return self.information[0][11]

    def track(self):
        self.mycursor.execute("select TrackingNumber,Sender from Parcel")
        myresult=self.mycursor.fetchall()
        for i,j in myresult:
            if self.TrackingNumber==i and self.UserID==j:
                self.mycursor.execute("select * from Parcel where TrackingNumber ='"+str(i)+"'")
                self.information =self.mycursor.fetchall()




