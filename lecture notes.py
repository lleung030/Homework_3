a_list=[1,2,3]
b_list=a_list[:]



def double_values(a_list):
    
    
    a_list=a_list[:]            # this makes a copy of the original list and then we can make changes to it without changing the original list 
    
    for i in range(len(a_list)):
        a_list= a_list[i]*2
    
    return a_list
input_list = [1,2,3,4]

double_values(input_list)

# string and tuple are immutable -------> no need to make a copy for a tuple or string

# lists need to make a copy because they are mutable


“{} has {} eyes”.format(key, val) 
# to format dictionary

print(f"The car that I drive is a {truck['year']} {truck['make']} {truck['model']}")
# using f string to format 
