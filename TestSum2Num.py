#write a unit test for a function that adds two numbers
import unittest

def add_2_numbers(x1,x2):
    return x1+x2

class test_sum(unittest.TestCase):
    def test_sum(self):
        self.assertEquals(add_2_numbers(2,3),5)
        self.assertEquals(add_2_numbers(2,0),2)
        self.assertEquals(add_2_numbers(2,-10),-8)
        self.assertNotEquals(add_2_numbers(12,13),5)
        self.assertEquals(add_2_numbers(12,13),26)

#driver code
if __name__=="main":
    unittest.main()
