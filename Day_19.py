#write a function to calculate factorial of a number

def factorial_recursive(num):
    if num==1:
        return 1
    elif(num>1):
        return factorial_recursive(num-1) * num
    
input_num=int(input("please enter a number: "))
factorial_result=factorial_recursive(input_num)
print("the factorial of {0} is {1}".format(input_num,factorial_result))
