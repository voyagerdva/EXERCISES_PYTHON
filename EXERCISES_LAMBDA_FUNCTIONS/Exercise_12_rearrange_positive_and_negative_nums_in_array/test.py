import unittest
from Exercise import Operations
import datetime

class testLambda(unittest.TestCase):

    def test_Rearrange(self):
        list1 = [-1, 2, -3, 5, 7, 8, 9, -10]
        ethalon = [2, 5, 7, 8, 9, -10, -3, -1]
        oper = Operations()
        result = oper.rearrange(list1)
        self.assertEqual(result, ethalon)

if __name__ == "__main__":
    unittest.main()