#write a program to shuffle the elements of a list randomly
import random

input=[34,23,53,43,22,1,3,5,98,122,3,54]
print("list before shuffle using random.shuffle() ")
print(input)
#using shuffle function from the random
random.shuffle(input)
print("list after shuffled using random.shuffle()")
print (input)


def randomize(arg):
    arg_list=arg.copy() #copy the argument list
    result_list=[]
    if isinstance(arg_list,list):
        for i in range(0,len(arg_list),1):
            x=random.randint(0,len(arg_list)-1)
            result_list.append(arg_list.pop(x))
    return result_list

input2=[3,45,33,12,53,65,46,999,43,15,70]
result_list2=randomize(input2)
print("list before shuffle using randomize function" )
print(input2)
print("list after shuffled using randomize function" )
print(result_list2)


