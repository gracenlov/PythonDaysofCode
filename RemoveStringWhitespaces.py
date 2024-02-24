#program that removes all whitespaces from a given string

string1="te st ing\n and this\t is \v another\r again"
def remove_whitespaces(string1):
  return string1.replace(" ","").replace("\n","").replace("\v","").replace("\t","").replace("\f","").replace("\r","")

print(remove_whitespaces(string1))


