#write a program to count the occurrences of a 
#specific character in a string

char_value=""

while True:
    input_value=input("Please enter a character: ")
    if len(input_value) ==1:
        char_value=input_value[0]
        break

string_value=input("Please enter a string: ")

count_occurences=0
if len(string_value)>0:
    for char in string_value:
        if char==char_value:
            count_occurences+=1

print("There {} occurrences of {}".format(count_occurences,char_value))
