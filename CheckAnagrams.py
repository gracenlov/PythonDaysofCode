#write a program to check if two strings are anagrams

import unittest

def check_anagrams(string1, string2):
    match=False
    #remove whitespaces
    string1 = ''.join(letter for letter in string1 if letter.isalnum())
    string1 = string1.replace("\n","").lower()
    string2 = ''.join(letter for letter in string2 if letter.isalnum())
    string2 = string2.replace("\n","").lower()
    dict_string1={}
    if(len(string1)==len(string2)):
        for x in string1:
            if x in dict_string1:
                dict_string1[x]+=1
            else:
                dict_string1[x]=1
        for x in string2:
            if(x in dict_string1):
                dict_string1[x]-=1
            else:
                return False
        for key in dict_string1:
            if(dict_string1[key]>0):
                return False
        return True

    return match


class test_anagrams(unittest.TestCase):
    def test_no_match_anagrams(self):
        self.assertEqual(check_anagrams("python","typhong"), False,"Check False ")

    def test_match_anagrams(self):
        self.assertEqual(check_anagrams("Python","typhon"), True,"Check True")
        self.assertEqual(check_anagrams("Vacation Time  ","i am not active\n"),True,"check true")

        self.assertEqual(check_anagrams("A decimal   point","I’m a dot in place\n"),True,"check true")


#driver code
if __name__=="__main__":
    unittest.main()
    
