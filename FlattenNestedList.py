#write a program to flatten a nested list

def flatten_nested_list(list_input):
    flatten_list=[]
    if(isinstance(list_input,list)):
        for x in list_input:
            if(isinstance(x,list)):
                for y in x:
                    flatten_list.append(y)
    return flatten_list



#driver code
if __name__=="__main__":
    user_input=[[1,5,10,12,90],["this","is", "my","test", "for", "nested"],
                [34.4,98,"hello","nested","world"],"ab"]
    result=flatten_nested_list(user_input)
    print("nested list", user_input)
    print("flatten nested list: ", result)
