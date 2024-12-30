from restaurent import *
from fooditem import FoodItem
class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
    
class Customer(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.past_orders=[]
        self.balance = 0
    
    def view_item(self,rest):
        rest.view_menu()

    def order(self,rest,item_name):
        item =rest.find_item(item_name)
        if item:
            self.past_orders.append(item)
            print('Here, enjoy your food')
        else:
            print('Food item not found')

    def view_bal(self):
        print(self.balance)
    
    def view_orders(self):
        for item in self.past_orders:
            print(f'Name: {item.name} Price: {item.price}')
    
    def add_mon(self,num):
        self.balance += num
        print(f"{num} is added to your balance. Total Money: {self.balance}")

    

class Admin:
    def __init__(self, name):
        self.name = name
    
    def add_new_item(self,rest,name,price):
        new_item = FoodItem(name=name,price=price)
        rest.add_item(new_item)

    def view_item(self,rest):
        rest.view_menu()
    
    def remove_item(self,rest,name):
        rest.remove_item(name)

    def add_cust(self,rest,name,email,address):
        new_cust = Customer(name,email,address)
        rest.add_cust(new_cust)

    def view_cust(self,rest):
        rest.view_cus_det()

    def rem_cust(self,rest,name):
        rest.remove_cust(name)

    def updt_price(self,rest,name,price):
        rest.update_item(name,price)
    
    



    

