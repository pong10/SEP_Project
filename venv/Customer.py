from Person import *
class Customer(Person):
    def __init__(self, name, address, phone, email):
        super().__init__(name,address,phone,email)
t=Customer('somphon','123456','092275229','manza1921@hotmail.com')
t.updateAddress('1649876')
t.printDetail()
