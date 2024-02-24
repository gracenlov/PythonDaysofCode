#write a function that checks if a number is prime
from math import sqrt


def isPrimeNum(x):
    if(x<2):
        return False
    #check from 2 to squrt(x)
    for i in range(2,int(sqrt(x))+1):
        if(x%i==0): #not a prime
            return False
    return True


print("Is Prime: ",isPrimeNum(3))
print("Is Prime: ",isPrimeNum(1))
print("Is Prime: ",isPrimeNum(2))
print("Is Prime: ",isPrimeNum(13))
print("Is Not Prime: ",isPrimeNum(8))
print("Is Not Prime: ",isPrimeNum(12))
print("Is Not Prime: ",isPrimeNum(64))
print("Is Not Prime: ",isPrimeNum(1))
