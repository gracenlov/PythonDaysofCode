#create a program to find the largest among three numbers

def find_largest_number(num1,num2,num3):
    largest=0
    if(num1>=num2 and num1>=num3):
        largest=num1
    elif(num2>=num1 and num2>=num3):
        largest=num2
    elif(num3>=num1 and num3>=num2):
        largest=num3
   
    return largest

input1=int(input("Enter first number: "))
input2=int(input("enter second number: "))
input3=int(input("enter third number: "))

result=find_largest_number(input1,input2,input3)
print("The largest number is {0}".format(result))
