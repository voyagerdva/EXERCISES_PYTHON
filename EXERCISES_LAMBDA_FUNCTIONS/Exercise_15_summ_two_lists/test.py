import unittest
from Exercise import Operations

class testListsSumm(unittest.TestCase):
    def test_Summ(self):
        originalList1 = [1,2,3]
        originalList2 = [4,5,6]
        ethalon = [5,7,9]

        oper = Operations()
        result = oper.listsSumm(originalList1, originalList2)
        self.assertEquals(result, ethalon)

if __name__ == '__main__':
    unittest.main()
