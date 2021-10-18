import unittest
from Exercise import Operations
import datetime

class testLambda(unittest.TestCase):

    def test_Intersection(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list2 = [1, 2, 4, 8, 9]
        ethalon = [1, 2, 4, 8, 9]
        oper = Operations()
        result = oper.intersection(list1, list2)
        self.assertEqual(result, ethalon)

if __name__ == "__main__":
    unittest.main()