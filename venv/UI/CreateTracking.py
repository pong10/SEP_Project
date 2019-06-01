import mysql.connector
#class Admin(Employee):
mydb = mysql.connector.connect(
    host="35.198.233.244",
    user="root",
    passwd="123456",
    database="parcelexpress",
    port="3306"
)
mycursor = mydb.cursor()

def createTrackingNumber(tracking_no,sender_firstname,sender_lastname,sender_address,sender_province,sender_postcode,sender_contact,receiver_firstname,receiver_lastname,receiver_address,receiver_province,receiver_postcode,receiver_contact,state):

    sender_name=sender_firstname+" "+sender_lastname
    receiver_name=receiver_firstname+" "+receiver_lastname
    command = "INSERT INTO Parcel(TrackingNumber,Sender,Sender_address,Sender_province,Sender_postcode,Sender_contact,Receiver,Receiver_address,Receiver_province,Receiver_postcode,Receiver_contact,State)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #tracking_id=  self.generate('TH')
    mycursor.execute(command,(tracking_no,sender_name,sender_address,sender_province,sender_postcode,sender_contact,receiver_name,receiver_address,receiver_province,receiver_postcode,receiver_contact,state))
    mydb.commit()


