#write a function that calculates the average of a list of numbers

def calculateAvg(numList):
    total=0
    avgValue=0
    listLength=len(numList)
    for num in numList:
        total+=num
    if(listLength>0):
        avgValue=total/listLength
        avgValue=round(avgValue,2)
    return avgValue

# Driver Code
if __name__ == '__main__':
 
    inputList=[12,4,34,32,90,3,8,4]
    result =calculateAvg(inputList)
    print(inputList)
    print("The average is ", result)

    inputList=[10,0,2,54,11,37,59]
    result =calculateAvg(inputList)
    print(inputList)
    print("The average is ", result)
