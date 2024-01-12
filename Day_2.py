#create a program to calculate the area of a circle given its radius

import math

#prompt input for the radius
radius=float(input("Enter a circle radius: "))

#Circle area=pi x r^2
circle_area=round(math.pi * radius * radius,2)

print("The area of the circle with radius={} is {}".format(radius,circle_area) )
