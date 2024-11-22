import unittest

from math_functions import add, subtract, power, division

#Unit Tests
class TestMathFunctions(unittest.TestCase):
    def test_division(self):
        #Reg Tests
        self.assertEqual(division(10, 4), 2.5)
        self.assertEqual(division(10, 2), 5)

        #Edge Cases
        self.assertEqual(division(10,0), 0)
        self.assertEqual(division(0,5), 0)
        self.assertEqual(division(-10,5), -2)
        self.assertEqual(division(-10,-5), 2)

    def test_power(self):
        #Reg Tests
        self.assertEqual(power(2,3), 8)
        self.assertEqual(power(3,2), 9)

        #Edges Cases
        self.assertEqual(power(5,0), 1)
        self.assertEqual(power(0,3), 0)
        self.assertEqual(power(1/2,2), 1/4)




    if __name__ == '__main__':
        unittest.main()
