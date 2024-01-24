#write a program to print the multiplication table of a given number

def get_multiplication_table(number):
    mult_table=[]
    if isinstance(number, int) | isinstance(number,float):
        i=1
        while i<=10:
            mult_table.append(number*(i))
            i+=1
    print( mult_table)
    return mult_table

number_arg = int(input("Enter a number:"))
mult_table_result=get_multiplication_table(number_arg)

i=0
while i<len(mult_table_result):
    print("{0} x {1} = {2}".format(number_arg,i+1,mult_table_result[i]))
    i+=1




 
