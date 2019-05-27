from Person import *
class Admin(Employee):
    def __init__(self, name, address, phone, email):
        super().__init__(name,address,phone,email)