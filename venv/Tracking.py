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

    def __init__(self,TrackingNumber,UserId):
        self.TrackingNumber=TrackingNumber
        self.UserID=UserId

    def trackPercent(self,state):
        i=20
        for i in range(0,5):
            if(self.state_of_parcel[i]==state):
                return i+20

    def track(self):
        State_information=''
        User_information=''
        self.mycursor.execute("select TrackingNumber,UserID from Tracking_ID")
        myresult=self.mycursor.fetchall()
        for i,j in myresult:
            if self.TrackingNumber==i and self.UserID==j:
                self.mycursor.execute("select State from Parcel where TrackingNumber ='"+str(i)+"'")
                State_information =self.mycursor.fetchall()
                self.mycursor.execute("select * from User where UserID ='"+str(j)+"';")
                User_information =self.mycursor.fetchall()
        print(self.trackPercent(State_information[0][0]))
        print(User_information)

t=Tracking('ABC1231245TH','13120')
t.track()



