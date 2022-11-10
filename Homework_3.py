# Exercises
# 1) Build a Shopping Cart 
# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input 
# 2) Stores user input into a dictionary or list 
# 3) The User can add or delete items 
# 4) The User can see current shopping list 
# 5) The program Loops until user 'quits' 
# 6) Upon quiting the program, print out all items in the user's list 


print("SHOPPING CART")


shopping_list=[]


running = True
while running:

    print("Select from list: 1.(a)/Add item  2.(d)Delete item  3.(v)Current shopping list  4.(q)Quit")
    
    choices = ['a', 'd', 'v', 'q', 'add', 'delete', 'view', 'quit']
    
    selection=input("Enter selection: ")
    
    if selection not in choices:
        print(f"{selection} is not a valid input. Please Add / Delete / View / Quit: ")
    else:
        running = False

    if selection.lower()=='a' or selection.lower()=='add':
       
        item=input("What item you want to add: ")
        
        shopping_list.append(item)
        
    elif selection.lower()=='d' or selection.lower()=='delete':
        
        item=input("Item you want to remove: ")
        
        shopping_list.remove(item)
        
    elif selection.lower()=='v' or selection.lower()=='view':
        
        print("In your BASKET: ", shopping_list)
        
    elif selection.lower()=='q' or selection.lower()=='quit':
        
        print(f'{shopping_list} Thank you for shopping with us! Please come again!')
        
        print("Thank you!!")
        
        break
    
    else:
        print("INVALID INPUT PLEASE TRY AGAIN!")


# 2) Create a Module in VS Code and Import It into jupyter notebook 
# Module should have the following capabilities:

# 1) Has a function to calculate the square footage of a house 
# Reminder of Formula: Length X Width == Area
# 2) Has a function to calculate the circumference of a circle 

from area import find_area

find_area()

# Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage

from dimensions import circumference

circumference()
