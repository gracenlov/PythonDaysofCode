#write a program that checks if a key exists in a dictionary

def check_key(dict, x_key):
    if x_key in dict:
        return True
    return False

user_dict={'Student':["David","Samuel","Terry","Evan"], 
           "Age":[27,24,22,32],
           "Country":["UK","Canada","China","USA"],
           "Course":["Python","Data Structures","Machine Learning","Web Development"], 
           "Marks":[85,72,89,76]}
search_key=input("Enter key to check: ")
result=check_key(user_dict,search_key)
if result==True:
    print("{0} exists in the dictionary keys".format(search_key, user_dict.keys))
else:
    print("{0} doesnot exists in the dictionary keys".format(search_key, user_dict.keys))
