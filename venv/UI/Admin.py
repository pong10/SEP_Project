from Person import *
import mysql.connector
import uuid
class Admin(Person):
#class Admin(Employee):
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
        front = 'PAE'
        body = uuid.uuid4().hex
        body = body.upper()[0:8]
        code = front + body + countrycode
        return code

    #def insertCreateDatabase(self,sender_firstname,sender_lastname,sender_address,sender_province,sender_postcode,sender_contact,receiver_firstname,receiver_lastname,receiver_address,receiver_province,receiver_postcode,receiver_contact):
    #    sender_name=sender_firstname+sender_lastname
    #    receiver_name=receiver_firstname+receiver_lastname
    #    command="insert into Parcel(Tracking_id,Sender,Sender_address,Sender_province,Sender_postcode,Sender_contact,Receiver,Receiver_address,Receiver_province,Receiver_postcode,Receiver_contact)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #    self.mycursor.execute(command,())

    def createTrackingNumber(self,tracking_no,sender_firstname,sender_lastname,sender_address,sender_province,sender_postcode,sender_contact,receiver_firstname,receiver_lastname,receiver_address,receiver_province,receiver_postcode,receiver_contact,state):

        sender_name=sender_firstname+sender_lastname
        receiver_name=receiver_firstname+receiver_lastname
        command = "INSERT INTO Parcel(TrackingNumber,Sender,Sender_address,Sender_province,Sender_postcode,Sender_contact,Receiver,Receiver_address,Receiver_province,Receiver_postcode,Receiver_contact,State)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #tracking_id=  self.generate('TH')
        self.mycursor.execute(command,(tracking_no,sender_name,sender_address,sender_province,sender_postcode,sender_contact,receiver_name,receiver_address,receiver_province,receiver_postcode,receiver_contact,state))
        self.mydb.commit()


#t=Admin("somphon","123456",'0922795229','manza1921@hotmail.com')
#t.createTrackingNumber("NNN","b","c","d","e","f","g","h","i","j","k","l","m","n")



