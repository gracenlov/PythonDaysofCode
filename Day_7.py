#write a program to check if a number is positive, negative, or zero


input_str=input("enter a number: ")
input_value=0

while True:
    try:
        input_value=float(input_str)
        break
    except ValueError:
        input_str=input("enter a number: ")


if input_value>0:
    print("the input {} is positive".format(input_value))
elif input_value==0:
    print("the input {} is zero".format(input_value))
elif input_value<0:
    print("the input {} is negative".format(input_value))
else:
    print("Invalid input '{}' entered ".format(input_value))

