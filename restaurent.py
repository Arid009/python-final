class Restaurent:
    def __init__(self,name):
        self.name = name
        self.food_list = []
        self.customers = []

    def add_item(self,item):
        self.food_list.append(item)
        print(f'{item.name} is added successfully')

    def add_cust(self,cust):
        self.customers.append(cust)
        print(f'{cust.name} is added successfully')

    def find_item(self,item_name):
        for item in self.food_list:
            if item_name.lower() == item.name.lower():
                return item
        return None
    def find_cust(self,cust_name):
        for cust in self.customers:
            if cust_name.lower() == cust.name.lower():
                return cust
        return None
    
    def remove_cust(self,cust_name):
        cust = self.find_cust(cust_name)
        if cust:
            self.customers.remove(cust)
            print('customer deleted')
        else:
            print('customer not found')

    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item:
            self.food_list.remove(item)
            print(f'{item_name} deleted')
        else:
            print(f'{item_name} not found')

    def update_item(self,item_name,price):
        item = self.find_item(item_name)
        if item:
            item.price = price
            print(f'{item_name} price is now {price}')
        else:
            print(f'{item_name} not found')
        
    def view_menu(self):
        print('here is your menu')
        print('Name\tPrice')
        for item in self.food_list:
            print(f'{item.name}\t{item.price}')
    

    def view_cus_det(self):
        print('Customers details')
        print('Name\tEmail\tAddress')
        for cust in self.customers:
            print(f'{cust.name}\t{cust.email}\t{cust.address}')
        