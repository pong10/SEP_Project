
class Person:
    def __init__(self,name,address,phone,email):
        self.Name=name
        self.Address=address
        self.Phone=phone
        self.Email=email
    def updateAddress(self,address):
        self.Address=address
    def updatePhone(self,phone):
        self.Phone=phone
    def updateEmail(self,phone):
        self.Email=email
    def printDetail(self):
        print('Name is ', self.Name)
        print('The phone number is ',self.Phone)
        print('The Address is ', self.Address)
        print('The email is ', self.Email)