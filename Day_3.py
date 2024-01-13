#create a function to count the number of vowels in a given string

import re

def count_vowel(stringVal):
    count =0
    vowels=['a','e','i','o','u']
    #check if the argument is string type
    if isinstance(stringVal,str)== True:
      for ch in stringVal:
         if str.lower(ch) in vowels: #convert to lowercase before compare
            count+=1
    else:
       print("Invalid data, please provide string argument!")  
    return count

def count_vowelRegEx(stringVal):
    count =0
    regex="[aeiouAEIOU]"
    #check if the argument is string type
    if isinstance(stringVal,str)== True:
      vowelsStr=re.findall(regex,stringVal)
      count=len(vowelsStr)
    else:
       print("Invalid data, please provide string argument!")  
    return count

#test with coun_vowel function
inputString=input("Please enter a string of characters: ")
x=count_vowel(inputString)
print("there's {} vowels in the string {}".format(x, inputString))

#test with regex
inputString=input("Please enter a string: ")
x=count_vowel(inputString)
print("there's {} vowels in the string {}".format(x, inputString))
