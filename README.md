# finalCapstone

<h2>Shoe Inventory Management System</h2>

<h4>Description</h4>
An inventory management system to manage a shoe warehouse. The stock manager can use this program to read inventory data from files, create new inventory product by capturing input from the user, view all the shoes in the warehouse, restock the shoes whose quantity is lowest, search shoe using product code, search shoe with the highest quantity.

<h4>Installation</h4>
The program consists of only 2 files. The main program is in inventory.py and the stock data is in inventory.txt.  Copy these 2 files and place them within a same folder. After that you can run the program using python command line or using PyCharm editor.

<h4>Usage</h4>
The program will present you with following menu, user can continously select an option until they press 'e' to exit the menu.


    Select one of the following Options below:

        hq - Show the product with highest quantity        
        vp - Show the value of each product        
        ss - Search the shoe        
        va - View all the shoes in the inventory
        cs - Capture the new shoe from the user
        rs - Re-Stock the shoe 
        e  - Exit
        :
 
 Here are few sample outputs from the program.
 
  
  ```pycon
  va - View All the shoes in the inventory
  ╒═════════════════════╤════════╤═══════════╤════════╤═══════════════╕
  │ Country             │   Code │ Product   │   Cost │ Quantity      │
  ╞═════════════════════╪════════╪═══════════╪════════╪═══════════════╡
  │ Air Max 90          │   2300 │ SKU44386  │     20 │ South Africa  │
  ├─────────────────────┼────────┼───────────┼────────┼───────────────┤
  │ Jordan 1            │   3200 │ SKU90000  │     50 │ China         │
  ├─────────────────────┼────────┼───────────┼────────┼───────────────┤
  │ Blazer              │   1700 │ SKU63221  │     19 │ Vietnam       │
  ├─────────────────────┼────────┼───────────┼────────┼───────────────┤
  │ Cortez              │    970 │ SKU29077  │     60 │ United States │
  ╘═══════════════════════════════════════════════════════════════════╘     
  ```
  
  ```pycon
  vp - show the Value of each Product
  ╒═════════════════════╤══════════════╕
  │ Product             │   Total Cost │
  ╞═════════════════════╪══════════════╡
  │ Air Max 90          │        46000 │
  ├─────────────────────┼──────────────┤
  │ Jordan 1            │       160000 │
  ├─────────────────────┼──────────────┤
  │ Blazer              │        32300 │
  ├─────────────────────┼──────────────┤
  │ Cortez              │        58200 │
  ╘════════════════════════════════════╘
 ```


<h4>Credits</h4>
This project has been developed by Monika Nohwar ( that is myself!!!!!)  

My many thanks to the **HyperionDev** for the guidance, course material and amazing mentorship for teaching the **Software Engineering** course.   
I have primarily learnt the **Python** language as part of this course and bootcamp and I have also learnt enormously from the comprehensive review comments on my assessments.
