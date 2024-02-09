#create a function that finds the second smallest element in a list

def find_second_smallest(userList):
    sortedList=[]
    result="Does not exist"
    if(len(userList)>1):
        sortedList=sorted(userList)
        print(sortedList)
        if(len(userList)==2):
            result=sortedList[0]
        else:
            result=sortedList[1]
    return result


userInput1=list(int(x) for x in input("enter list 1 using comma separated: ").split(","))
print(userInput1)

result=find_second_smallest(userInput1)
print("The second smallest element in the list: ",result)
