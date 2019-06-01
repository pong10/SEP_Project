from Person import *
class Employee(Person):
    def __init__(self, name, address, phone, email):
        super().__init__(name,address,phone,email)