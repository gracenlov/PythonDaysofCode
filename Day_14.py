#write a program to print the first n numbers of Fibonacci sequence

def Fibonacci_recursive(arg):
    result=int(0)
    if(arg==1):
        result=arg
    elif(arg==0):
        result=arg
    elif(arg>1):
        result=Fibonacci_recursive(arg-1) + Fibonacci_recursive(arg-2)
    return result


def Fibonacci_Recurse(arg):
   result_list=[]
   for i in range(arg):
      result_list.append(Fibonacci_recursive(i))
   return result_list

print(Fibonacci_Recurse(15)) #using recursive


def Fibonacci(arg):
    fib_list_arg=[] #assign empty list first
   
    if(arg>0 & isinstance(fib_list_arg,list)):
        for i in range(1,arg+1):
            if(i==1):
             fib_list_arg.append(i-1)
            elif(i==2):
             fib_list_arg.append(i-1)
            elif(i>=3):
                fib_list_arg.append(fib_list_arg[i-2] + fib_list_arg[i-3])
    return fib_list_arg



n=0
while(isinstance(n,int)):
    n=int(input("Provide a number to generate Fibonacci sequence: "))
    fib_list=Fibonacci(n)
    print("The Fibonacci sequence: ")
    print(fib_list)
    
