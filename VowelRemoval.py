#write a program to remove vowels from a given string

def vowel_removal(user_string):
    vowels="aeiou"
    new_string=""
    if(isinstance(user_string,str)):
        for ch in user_string:
            if(ch.lower() in vowels)==False :
                new_string=new_string + ch
    return new_string



user_input=input("Please enter a string: ")
result=vowel_removal(user_input)
print("string without vowels: ", result)
