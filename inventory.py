from tabulate import tabulate
import time

#========The beginning of the Shoe class==========
class Shoe:
    '''
    The constructor of Shoe class. Initialise the shoe wih : country, code, product, cost, quantity
    '''
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    '''
    This Shoe class function will return the cost of the Shoe
    '''
    def get_cost(self):
        return self.cost

    '''
    This Shoe class function will return the quantity of the Shoe
    '''
    def get_quantity(self):
        return self.quantity

    '''
    This function will return the String representation of the Shoe class.
    '''
    def __str__(self):
        return f"Shoe : Product - '{self.product}', Cost - '{self.cost}', Code - '{self.code}', Quantity - '{self.quantity}', Country - '{self.country}'"


#The definition of the Shoe class has completed here.

#==========Functions outside the class==============

'''
The shoe_list will be used to store a list of objects of shoes.
'''
shoe_list = []

'''
This function will read the shoes data from file 'inventory.txt'.
The function will create a 'Shoe' object from each line which has got comma separated attributes
All these Shoe objects will be stored in shoe_list
If the input file is not found then an appropriate message is given to the user
'''
def read_shoes_data():
    file_line_num = 0

    try:
        with open("inventory.txt", "r+") as invty_file:
            for line in invty_file.readlines():
                file_line_num = file_line_num + 1
                if file_line_num == 1:
                    continue  # Skipping the 1st line of file

                line_split = line.split(",")
                shoe = Shoe(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4].strip())
                shoe_list.append(shoe)
    except FileNotFoundError:
        msg = "Sorry, the file 'inventory.txt' " + "does not exist."
        print(msg)

'''
This function will create a new Shoe object by asking user for the appropriate attributes.
This new shoe will be added to the shoe_list
'''
def capture_shoes():
    u_country = input("Enter the country of produce for the shoe ?")
    u_code = input("Enter the code of the shoe ?")
    u_product = input("Enter the product for the shoe ?")
    u_cost = input("Enter the cost of the shoe ?")
    u_quantity = input("Enter the quantity for the shoe ?")
    shoe = Shoe(u_country, u_code, u_product, u_cost, u_quantity)
    shoe_list.append(shoe)
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

'''
This function will view all the shoes in the inventory. 
It uses tabulate method for formatting. 
'''
def view_all():
    shoe_list_tabulate = []
    count = 0
    for shoe in shoe_list:
        shoe_list_tabulate.append([shoe.product, shoe.cost, shoe.code, shoe.quantity, shoe.country])

    heads = ["Country","Code","Product","Cost","Quantity"]
    print("\033[34m",tabulate(shoe_list_tabulate, headers=heads, tablefmt='fancy_grid'))

    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

'''
This function will restock the product which has the lowest quantity in the inventory. 
It will first display the product with the lowest quantity and then ask user how much to restock.
It will then rewrite the new inventory in the 'inventory.txt' file.
'''
def re_stock():
    lowest_quantity_shoe = highest_qty(False)

    for shoe in shoe_list:
        if int(shoe.quantity) < int(lowest_quantity_shoe.quantity):
            #lowest_quantity = shoe.quantity
            lowest_quantity_shoe = shoe

    print(f"\nThe shoe with the lowest quantity is {lowest_quantity_shoe}")
    restock_quantity = int(input("How much quantity you want to restock for this shoe ?"))
    lowest_quantity_shoe.quantity = int(lowest_quantity_shoe.quantity) + restock_quantity

    with open("inventory.txt","w+") as inv_file:
        inv_file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            inv_file.write(shoe.country + "," + str(shoe.code)
                           + ","+ str(shoe.product) + "," + str(shoe.cost)
                           + ","+ str(shoe.quantity) + "\n")

    print(f"The product has been restocked. Press 'va' to view the inventory again")
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def seach_shoe():
    u_code = input("Enter the shoe code that you want to search :")
    show_found_flag = False
    for shoe in shoe_list:
        if shoe.code.lower() == u_code.lower():
            print(f"Here you got with your searched shoe : \n {shoe}")
            show_found_flag = True
            break

    if show_found_flag != True:
        print(f"There is no shoe with the provided code")

    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    product_totalcost_list = []
    for shoe in shoe_list:
        value = int(shoe.cost) * int(shoe.quantity)
        product_totalcost_list.append([shoe.product,value])
        #print(f"The total value for product {shoe.product} is {value}")

    heads = ["Product", "Total Cost"]
    print(tabulate(product_totalcost_list, headers=heads, tablefmt='fancy_grid'))
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

'''
This function will print the Shoe with the highest quantity
'''
def highest_qty(print_flag):
    max_quantity = 0
    shoe_highest_quantity = None
    for shoe in shoe_list:
        if int(shoe.quantity) > max_quantity:
            shoe_highest_quantity = shoe
            max_quantity = int(shoe.quantity)

    if print_flag == None or print_flag == True:
        print(f"The shoe on the sale is : {shoe_highest_quantity}")

    return shoe_highest_quantity

    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''


read_shoes_data()    #Firstly, create the inventory
'''
Presenting the 'Shoe' menu to the user. 
It will ask the user's input to view shoes, capture shoe, restock shoe, search shoe, highest quantity, product value
After displaying results, it will wait for 2 seconds and then show the menu again to the user. 
'''
while True:
    menu = input('''\nSelect one of the following Options below:
        hq - Show the product with highest quantity
        vp - Show the value of each product
        ss - Search the shoe
        va - View all the shoes in the inventory
        cs - Capture the new shoe from the user
        rs - Re-Stock the shoe 
        e - Exit
    : ''').lower()

    if menu == 'hq':
        highest_qty(True)
        time.sleep(2)
    elif menu == 'vp':
        value_per_item()
        time.sleep(2)
    elif menu == 'ss':
        seach_shoe()
        time.sleep(2)
    elif menu == 'va':
        view_all()
        time.sleep(2)
    elif menu == 'cs':
        capture_shoes()
        time.sleep(2)
    elif menu == 'rs':
        re_stock()
        time.sleep(2)
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")
        time.sleep(2)
