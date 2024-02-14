#write  a program to merge 2  dictionaries

def merge_dictionary(x1,x2):
        x1.update(x2)
        return x1

dict1={1924:"Rat",1925:"Ox",1926:"Tiger",
       1927:"Rabbit",1928:"Snake",1929:"Dragon",
        1930:"Horse", 1931:"Goat", 1932:"Monkey",
        1933:"Rooster", 1934:"Dog",1935:"Pig"}
dict2={2020:"Rat",1925:"Ox",1926:"Tiger",
       2011:"Rabbit",2013:"Snake",1977:"Dragon",
        1978:"Horse", 1931:"Goat", 1932:"Monkey",
        2029:"Rooster", 1982:"Dog",1983:"Pig"}

result=merge_dictionary(dict1,dict2)
print(result)
