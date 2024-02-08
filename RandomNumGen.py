#create a function that generates a random number between a given range
import random

def generateRandNum(start,end):
    result=0
    if(end<start):
        raise ValueError("The range {0} - {1} is invalid.".format(start,end))
    else:
        result=random.randrange(start,end)
    return result


num1=int(input("enter the start of the range:"))
num2=int(input("enter then end of the range:"))
result=generateRandNum(num1,num2)
print("a random number generated: ",result)
