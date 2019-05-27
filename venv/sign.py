import mysql.connector
class SignUp():
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
    def __init__(self, user, password):
        self.user = user
        self.password = password
    def UserExist(self):
        print("user exist")
    def binarySearch(self,arr, l, r, x):
        print("this is binary search")