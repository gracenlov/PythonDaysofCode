#write a function to find the largest 
#common divisor of two numbers using a function

import math

def Find_lcd_mathLib(x,y):
  return math.gcd(x,y);

def FindLargetDivisor(x,y):
  largest_num=x
  second_num=y
  #determine if x or y is the largest
  if(x<y):
    largest_num=y
    second_num=x
  temp_denominator=second_num;
  while((second_num%temp_denominator!=0 
        or largest_num%temp_denominator!=0)
        and temp_denominator>0):
    temp_denominator-=1
  return temp_denominator

input1=36
input2=12
commonDivisor=FindLargetDivisor(input2,input1)
print("common divisor for {0} and {1} is {2}".format(input1, input2, commonDivisor))
print("USE Prebuilt math.gcd() -- common divisor for {0} and {1} is {2}".format(input1, input2, Find_lcd_mathLib(input1,input2)))
    
input1=49
input2=7
commonDivisor=FindLargetDivisor(input2,input1)
print("common divisor for {0} and {1} is {2}".format(input1, input2, commonDivisor))
print("USE Prebuilt math.gcd() -- common divisor for {0} and {1} is {2}".format(input1, input2, Find_lcd_mathLib(input1,input2)))
