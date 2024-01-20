#write a program to remove duplicates from a list

def remove_duplicate(values):
    return list(dict.fromkeys(values))


my_input=["a","4","b","c","c","a", "5","z","5","43","df","fd"]
my_list=remove_duplicate(my_input)

print("result with no duplicates: ",my_input)

print("result with no duplicate: ",my_list)
