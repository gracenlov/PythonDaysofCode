#Create a program to check if a number is even or odd

def CheckEvenOddNum(inputNum):
    if isinstance(inputNum,int):
        if inputNum%2==0:
            return True
        
    return False

val=0
while True:
    try:
        val=int(input("please enter a number: "))
        result=CheckEvenOddNum(val)
        if result:
            print("The value {} is even number".format(val))
        else:
            print("The value {} is odd number".format(val))
        continue
    except ValueError:
        break
       
        

        
