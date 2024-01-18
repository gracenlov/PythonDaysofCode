#write a function that accepts a string and calculates the 
#number of uppercase and lowercase letter in it

def caculate_stringcases (str_value):
    count_lower=0;
    count_upper=0;
    if isinstance(str_value,str):
         for char in str_value:
            if char.isupper():
                count_upper+=1
            elif char.islower():
              count_lower+=1
    return count_lower,count_upper

x="This is MY testing STRING for UPPER and lower characters."
result=caculate_stringcases(x)
print("There're {} uppercase and {} lowercase characters.".format(result[1],result[0]))
    

