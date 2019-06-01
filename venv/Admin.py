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
        front = 'PAE'
        body = uuid.uuid4().hex
        body = body.upper()[0:8]
        code = front + body + countrycode
        return code

    def createTrackingNumber(self,tracking_id,sender_firstname,sender_lastname,sender_address,sender_province,sender_postcode,sender_contact,receiver_firstname,receiver_lastname,receiver_address,receiver_province,receiver_postcode,receiver_contact):
        sender_name=sender_firstname+sender_lastname
        receiver_name=receiver_firstname+receiver_lastname
        command = "insert into Parcel(TrackingNumber,Sender,Sender_postcode,Sender_address,Sender_province,Sender_contact,Receiver,Receiver_address,Receiver_province,Receiver_postcode,Receiver_contact)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.mycursor.execute(command,(tracking_id,sender_name,sender_postcode,sender_address,sender_province,sender_contact,receiver_name,receiver_address,receiver_province,receiver_postcode,receiver_contact))
        self.mydb.commit()


t=Admin("somphon","123456",'0922795229','manza1921@hotmail.com')
t.createTrackingNumber('112334566','somphon','rueangsri','57/4','bankokok','12000','08245245','Pong','Buffalo','57/8','adsfdsaf','13120','2448484')