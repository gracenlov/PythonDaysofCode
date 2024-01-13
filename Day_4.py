#create a program to find the sum of all elements in a list

num_list=[3,4,5,9,10,43,67,65,3]

def sum_elements(elements):
    try:
        return sum(elements)
    except TypeError:
        print("Invalid data type in the list")
        return

print(sum_elements(num_list))
