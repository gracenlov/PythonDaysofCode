#create a program that checks if a given string is a valid email address

import re
 
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
 

def checkEmailFormat(emailAddress):
 
    if(re.fullmatch(regex, emailAddress)):
        print("Valid Email")
 
    else:
        print("Invalid Email")
 
# Driver Code
if __name__ == '__main__':
 
    email = "cashewYuPik@gmail.com"
 
    checkEmailFormat(email)
 
    email = "my.manager@everlasting-domain.net"
    checkEmailFormat(email)
 
    email = "ltrnguy45.com"
    checkEmailFormat(email)
