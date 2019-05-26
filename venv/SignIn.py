import mysql.connector
class SignIn_signUp():
    mydb = mysql.connector.connect(
        host="35.198.233.244",
        user="root",
        passwd="123456",
        database="parcelexpress",
        port="3306"
    )
    mycursor = mydb.cursor()
    #user = ''
    #password = ''
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def binarySearch(self,arr, l, r, x):
        # Check base case
        if r >= l:
            mid = l + (r - l) // 2
            # If element is present at the middle itself
            if arr[mid][mid] == x:
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

    def SignIn(self):
        self.mycursor.execute("SELECT Username,Password from Customer")
        myresult=self.mycursor.fetchall()
        for i,j in myresult:
            if self.user==i and self.password==j:
                return True
        return False


a=SignIn_signUp( 'Pong','123456')
print(a.SignIn())