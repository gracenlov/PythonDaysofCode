#write a program to reverse a given string

def reverse_string(string_input):
    i=len(string_input)-1
    string_reversed = ""
    while i>0:
     string_reversed = string_reversed + string_input[i]
     i-=1
     if(i==0):
        string_reversed = string_reversed + string_input[0]
    return string_reversed

def reverse_string_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string_recursion(s[1:]) + s[0]
    

str_arg="This is my String"
print("string value is " + str_arg)
print("string reversed is " + reverse_string(str_arg))

str_arg="Jesus loves you"
print("string value is " + str_arg)
print("string reversed is " + reverse_string_recursion(str_arg))
