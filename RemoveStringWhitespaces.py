#program that removes all whitespaces from a given string

string1="te st ing\n and this\t is \v another"
def remove_whitespaces(string1):
  return string1.replace(" ","").replace("\n","").replace("\v","").replace("\t","")

print(remove_whitespaces(string1))
