create a program that uses a lambda function to square each element of a list.

squareLamb=lambda a: a*a

userInput1=list((int(x) for x in input("enter list 1 using comma separated: ").split(",")))
print(userInput1)
result_list=[]

for x in userInput1:
    result_list.append(squareLamb(x))

print("Squared results: ", result_list)
