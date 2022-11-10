
print("SHOPPING CART")


shopping_list=[]


# running = True
# while running:

while True:
    
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
        
        print(f'Here is your receipt for these items: {shopping_list} Thank you for shopping with us! Please come again!')
        
        print("Thank you!!")
        
        break
    
    else:
        print("INVALID INPUT PLEASE TRY AGAIN!")
        
 



# address_book = []

# def store_user_info(name, address, city):
#     # address_book[key] = val\n",
#     address_book.append({
#         'name': name,
#         'address': address,
#         'city': city
#     })
        
# def main():
#     application_running = True
    
#     while application_running:
        
#         name = input("Person's Name: ")
#         address = input("Person's Address: ")
#         city = input("Person's City: ")
            
        
#         store_user_info(name, address, city)
    
#         while True:
            
#             quit = input("Would you like to quit? (Y/N)").lower()

#             if quit == 'y':
                
#                 print(address_book)
                
#                 application_running = False
            
        
            
#             elif quit == 'n':
#                 break
#             else:
#                 print(f"{quit} is not a valid option, please try again.")


# main()

