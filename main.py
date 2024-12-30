from restaurent import *
from users import *
from fooditem import FoodItem

foodsandcolor = Restaurent("Foods & Color")
item1 = FoodItem('bhat',12)
item2 = FoodItem('ice',20)
foodsandcolor.add_item(item1)
foodsandcolor.add_item(item2)

def cust_menu():
    name = input('Enter your Name: ')

    flag = foodsandcolor.find_cust(name)
    if flag:
        while True:
            print(f"Welcome {flag.name}!!")
            print("1. View Menu")
            print("2. Place Order")
            print("3. View Past Order")
            print("4. Add Balance")
            print("5. View Balance")
            print("6. Exit")
            
            choice = int(input("Enter Your Choice : "))
            if choice == 1:
                flag.view_item(foodsandcolor)
            elif choice == 2:
                item_name = input("Enter item name : ")
                flag.order(foodsandcolor, item_name)
            elif choice == 3:
                flag.view_orders()
            elif choice == 4:
                num = int(input("Enter the amount: "))
                flag.add_mon(num)
            elif choice == 5:
                flag.view_bal()
            elif choice == 6:
                break
            else:
                print("Invalid Input")
    else:
        print('you are not a customer')

def admin_menu():
    name = input("Enter Your Name : ")
    admin = Admin(name=name)
    
    while True:
        print(f"Welcome {admin.name}!!")
        print("1. Add New Item")
        print("2. Add New Customer")
        print("3. View Customers")
        print("4. View Items")
        print("5. Remove Item")
        print("6. Remove Customer")
        print("7. Update Item Price")
        print("8. Exit")

        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            name = input("Enter Item Name : ")
            price = int(input("Enter Item Price : "))
            admin.add_new_item(foodsandcolor,name,price)
        elif choice == 2:
            name = input("Enter Customer Name : ")
            email = input("Enter Customer email : ")
            address = input("Enter Customer address : ")
            admin.add_cust(rest=foodsandcolor,name=name,email=email,address=address)
        elif choice == 3:
            admin.view_cust(foodsandcolor)
        elif choice == 4:
            admin.view_item(foodsandcolor)
        elif choice == 5:
            name = input("Enter Item Name : ")
            admin.remove_item(foodsandcolor,name)
        elif choice == 6:
            name = input("Enter Customer Name : ")
            admin.rem_cust(foodsandcolor,name)
        elif choice == 7:
            name = input("Enter Item Name : ")
            price = int(input("Enter Item Price : "))
            admin.updt_price(foodsandcolor,name,price)
        elif choice == 8:
            break
        else:
            print("Invalid Input")

while True:
    print("Welcome to Foods & Color!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        cust_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input!!")