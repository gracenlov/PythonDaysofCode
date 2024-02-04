#creatte a progrma to concatenate 2 lists

def concatList(list1,list2):
    if(isinstance(list1,list) and isinstance(list2,list)):
        list1.extend(list2)
    
    return list1


userInput1=list(input("enter list 1 using comma separated: ").split(","))
userInput2=list(input("enter list 2 using comma separated: ").split(","))

print(userInput1)
print(userInput2)

result=concatList(userInput1,userInput2)
print(result)
