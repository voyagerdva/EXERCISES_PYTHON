import unittest
from Exercise import Operations
import datetime

class testLambda(unittest.TestCase):

    def test_Count_Even(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 15]
        ethalon = 4
        oper = Operations()
        result = oper.count_even(list1)
        self.assertEqual(result, ethalon)

    def test_Count_Odd(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 15]
        ethalon = 7
        oper = Operations()
        result = oper.count_odd(list1)
        self.assertEqual(result, ethalon)

if __name__ == "__main__":
    unittest.main()