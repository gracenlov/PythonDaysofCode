#create a program to find the maximum and minimum values in a list


list=[3,9,212,-4,-90,43,542,1003]

min_value=min(list)
max_value=max(list)
print("The minimum value from the list is {} and the maximum value from the list is {}".format(min_value,max_value))

#get user input
input_list=input("Enter list of number separated by a space: ")
user_list=input_list.split()
for i in range(len(user_list)):
    user_list[i]=int(user_list[i])

min_value=min(user_list)
max_value=max(user_list)
print("The minimum value from the list is {} and the maximum value from the list is {}".format(min_value,max_value))
