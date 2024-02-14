#write a test case for a function that checks if a number is prime
from math import sqrt
import unittest


def isPrimeNum(x):
    if(x<2):
        return False
    #check from 2 to squrt(x)
    for i in range(2,int(sqrt(x))+1):
        if(x%i==0): #not a prime
            return False
    return True

class TestIsPrime(unittest.TestCase):
    def test_isPrime(self):
        self.assertEqual(isPrimeNum(2),True)
        self.assertEqual(isPrimeNum(3),True)
        self.assertEqual(isPrimeNum(13),True)
        self.assertEqual(isPrimeNum(5),True)

        
    def test_isNotPrime(self):
        self.assertEqual(isPrimeNum(0),False)
        self.assertEqual(isPrimeNum(1),False)
        self.assertEqual(isPrimeNum(8),False)
        self.assertEqual(isPrimeNum(64),False)
        self.assertEqual(isPrimeNum(12),False)


# Driver Code
if __name__ == '__main__':
    unittest.main()
