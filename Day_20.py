#write a function that takes a list of numbers and returns a new list containing only the even numbers

def get_even_numbers_list(num_list):
    even_num_list=[]
    for num in num_list:
        #check the number is even
        if num%2==0:
            even_num_list.append(num)
    return even_num_list

user_input=[int(item) for item in input("Enter a list of numbers separated by comma: ").split(",")]

#temp=[12,2,255,24,54,55,56,58,57,17,55,77,79,36,37,35]
print("list of numbers: ", user_input)
result_list=get_even_numbers_list(user_input)
print("even number list: ", result_list)
