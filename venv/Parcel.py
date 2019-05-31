import mysql.connector
class Parcel():
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
    def __init__(self,Tracking_number,name):
        self.TrackingNo=Tracking_number
        self.Name=name
        self.current_state=''

    def setstate(self, state):
        self.current_state=state

    def getstate(self):
        return self.current_state

    def getAllParcelFromProvince(self,Province):
        self.mycursor.execute("SELECT TrackingNumber,currentLocation from Parcel")
        tracking_number=[]
        myresult = self.mycursor.fetchall()
        for i,j in myresult:
            if(j == Province):
                tracking_number.append(i)
        return tracking_number

    def printstate(self):
        for i in range(0,4):
            if(self.current_state==self.state_of_parcel[i]):
                break
            else:
                print(self.state_of_parcel[i])
t=Parcel("123456",'Somphon')
print(t.getAllParcelFromProvince('Chiang_Mai'))