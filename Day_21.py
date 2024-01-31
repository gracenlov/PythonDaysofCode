#create a program to remove a specific element from a set


def remove_list_item(item_list,item_delete):
    item_list = [ele for ele in item_list if ele != item_delete]
    return item_list


user_input=input("get a list of comma separated items: ")
items_list=user_input.split(",")
x=input("Enter item to be removed from the list:{}".format(items_list))
items_list=remove_list_item(items_list,x)
print(items_list)
