#create a program that check if a year is a leap year

#To determine whether a year is a leap year, follow these steps:

#1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
#2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
#3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
#4. The year is a leap year (it has 366 days).
#5. The year is not a leap year (it has 365 days).

def check_leap_year(year_val):
    leap_year=False
    if(year_val>0):
        if(year_val%4==0):
            if(year_val%100==0):
                if(year_val%400==0):
                    leap_year=True
                else:
                    leap_year=False
            else:
                leap_year=True
        else:
            leap_year=False
    return leap_year


year_input=2024
while(isinstance(year_input,int)):
    year_input=int(input("Please enter a year: "))
    if(check_leap_year(year_input)):
        print("Year: {} is a leap year".format(year_input))
    else:
        print("Year: {} is not a leap year".format(year_input))
