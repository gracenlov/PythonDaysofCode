#create a program that removes the nth element from a list


def removeNthElement(xList,nthEle):
    if(nthEle=<len(userInput1) and nthEle>0):
        xList.pop(nthEle-1)
    return xList

userInput1=list(x for x in input("enter list 1 using comma separated: ").split(","))
nthElement=int(input("enter element # to be removed:"))
print(userInput1)

result_list=removeNthElement(userInput1,nthElement)

print("list: ", result_list)
