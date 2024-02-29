#Write a program that reads an integer from the user and handles invalid inputs

try:
    x=int(input("Enter integer: "))
    print("Integer input: ",x)
except ValueError as e:
    print("Invalid inputs not integer: ", e)
