
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost
        '''
        Add the code to return the cost of the shoe in this method.
        '''

    def get_quantity(self):
        return self.quantity
        '''
        Add the code to return the quantity of the shoes.
        '''

    def __str__(self):
        return f"The product {self.product} has cost {self.cost} and total quantity is {self.quantity} . Its code is {self.code} and country of origin is {self.country}"
        '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    file_line_num = 0
    with open("inventory.txt","r+") as invty_file:
        for line in invty_file.readlines():
            if file_line_num == 0:
                continue    #Skipping the 1st line of file
            file_line_num += 1
            line_split = line.split(",")
            shoe = Shoe(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4])
            shoe_list.append(shoe)
    # use try exceptoin block arun
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
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

def view_all():
    for shoe in shoe_list:
        print(shoe)
        #arun use tabulate module
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def re_stock():
    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def seach_shoe():
    u_code = input("Enter the code of the shoe that you want to search :")

    for shoe in shoe_list:
        shoe_str = str(shoe)
        if shoe_str.lower() == u_code.lower():
            return shoe

    #If shoe not found arun

    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''