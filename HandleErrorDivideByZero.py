#program that uses try-except block to handle division by zero

def division(denominator,numerator):
  result=0
  try:
    result=numerator/denominator
    print(numerator, "/", denominator, "=",result)
  except ValueError as e:
    print("Error: ",e)
  except ZeroDivisionError as e:
    print("Error: ",e)

division(0,3)
division(7,0)
division(7,49)
