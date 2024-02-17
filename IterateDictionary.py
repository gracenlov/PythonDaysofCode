#Write a program to iterate through a dictionary and print its keys and values

def print_Keys_Values_Dictionary(dict1):
    if(isinstance(dict1,dict)):
        for key, value in dict1.items():
            print("Key: {0}, Value: {1} ".format(key,value))


#driver code
if __name__=="__main__":
    input_dict={"fruit":["banana","apple","grape","pineapple"], 
                "vegetable":["Kale","carrot","spinach"], 
                "spices":["five spices", "salt", "sugar","pepper"],
                "sauces":["ketchup","soy sauce", "fish sauce"]}
    print_Keys_Values_Dictionary(input_dict)
