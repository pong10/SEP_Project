import mysql.connector
class Register():

    mydb = mysql.connector.connect(
        host="35.198.233.244",
        user="root",
        passwd="123456",
        database="parcelexpress",
        port="3306"
    )
    mycursor = mydb.cursor()
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def SignIn(self):
        self.mycursor.execute("SELECT Username,Password from Customer")
        myresult=self.mycursor.fetchall()
        print(myresult)

    def binarySearch(self,arr, l, r, x):
        # Check base case
        if r >= l:
            mid = l + (r - l) // 2
            # If element is present at the middle itself
            if arr[mid][0] == x:
                return True
            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid][0] > x:
                return self.binarySearch(arr, l, mid - 1, x)
                # Else the element can only be present in right subarray
            else:
                return self.binarySearch(arr, mid + 1, r, x)
        else:
            # Element is not present in the array
            return False

    def UserExist(self):
        self.mycursor.execute("SELECT  Username FROM Customer")
        myresult=self.mycursor.fetchall()
        t = self.binarySearch(myresult,0,len(myresult),self.user)
        if t == True:
            return True
        else:
            return False
    def signIn(self):
        self.

    def signUp(self):
        if(self.UserExist()==False):
          sql = "INSERT INTO Customer(Username,Password) VALUES (%s, %s)"
          val = (self.user, self.password)
          self.mycursor.execute(sql, val)
          self.mydb.commit()
        else:
          raise InValid('User is already exist')

    def print(self):
        self.mycursor.execute("SELECT Username, Password FROM Customer")
        myresult = self.mycursor.fetchall()

        for x in myresult:
            print(x)
a=SignIn_signUp( 'Somphon','123456')
a.SignIn()


# mycursor.execute("SELECT Username, Password FROM Customer")
# myresult = mycursor.fetchall()
#
# for x in myresult:
#  print(x)
# sql = "INSERT INTO Customer(Username,Password) VALUES (%s, %s)"
# val = ("Somphon", "123456")
# mycursor.execute(sql, val)
# mydb.commit()
# print("1 record inserted, UserId:", mycursor.lastrowid)
# mycursor.execute("CREATE TABLE Customer (UserId INT AUTO_INCREMENT PRIMARY KEY,Username VARCHAR(20),Password VARCHAR (20))")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#  print(x)
# mycursor=mydb.cursor()
# mycursor.execute("CREATE TABLE User(Username VARCHAR(255),Password VARCHAR(255),
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#    print(x)