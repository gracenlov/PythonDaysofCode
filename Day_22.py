#write a program to find the second largest element in a list

def second_max(my_list):
    x=len(my_list)
    if(x==1):
        return my_list[0]
    elif(x==0):
        return 0
    
    my_list.sort()
    print(my_list)
    return my_list[-2]

#O(n) algorithm to find second max item
def second_max1(my_list):
    x=len(my_list)
   
    if(x==1):
        return my_list[0]
    elif(x==0):
        return 0

    max_value=max(my_list[0],my_list[1])
    second_max=min(my_list[1],my_list[0])
    for i in range(2,x):
        if (my_list[i]>max_value):
            max_value=my_list[i]
            second_max=max_value
        elif ((my_list[i] > second_max) and (my_list[i]!=max_value)):
            second_max=my_list[i]
        elif ((my_list[i]!=second_max) and (second_max==max_value)):
            second_max=my_list[i]
    
    return second_max
            


user_input=input("get a list of comma separated items: ")
items_list=[int(item) for item in user_input.split(",")]
result_list=second_max(items_list)
print("The second largest item in the list is " ,result_list)

user_input=input("get a list of comma separated items: ")
items_list=[int(item) for item in user_input.split(",")]
result_list=second_max1(items_list)
print("The second largest item in the list is " ,result_list)
