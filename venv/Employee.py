from Person import *
class Employee(Person):
    def __init__(self, name, phone, email, province):
        super().__init__(name,phone,email,province)