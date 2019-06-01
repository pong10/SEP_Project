import mysql.connector
class showHistory():
    mydb = mysql.connector.connect(
        host="35.198.233.244",
        user="root",
        passwd="123456",
        database="parcelexpress",
        port="3306"
    )

    mycursor = mydb.cursor()
    def __init__(self,sender):
        self.username=sender
        self.history=[]


    def GetDetail(self):
        lst=[]
        lst_get=[]
        c=0
        self.mycursor.execute("select Sender from Parcel")
        myresult=self.mycursor.fetchall()
        DataUser=[x[0] for x in myresult]
        for i in DataUser:

            if i==self.username:
                lst.append(i)

        for i in lst:

            command="select TrackingNumber,Sender,Sender_province,Receiver,Receiver_province from Parcel where Sender ='" + i +"'";
            self.mycursor.execute(command)
            results = self.mycursor.fetchall()
            for i in results:
                lst_get.append(i)
                lst_get.append(i)
        for i in range(0, len(lst_get)):
            self.history.append([])
            self.history[c].append(lst_get[i][0])
            self.history[c].append(lst_get[i][1])
            self.history[c].append(lst_get[i][2])
            self.history[c].append(lst_get[i][3])
            self.history[c].append(lst_get[i][4])
            c = c + 1
        return self.history
    def getTrackingNumber(self):
        for i in range(0,len(self.history)):
            return self.history[i][0]

t=showHistory('Arun123456')








