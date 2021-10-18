import unittest
from Exercise import Operations



class testLambda(unittest.TestCase):

    def test_even(self):
        subject_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        subject_ethalon = [2, 4, 6, 8, 10]
        oper = Operations()
        result = oper.filterEven(subject_original)
        self.assertEqual(result, subject_ethalon)

    def test_odd(self):
        subject_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        subject_ethalon = [1, 3, 5, 7, 9]
        oper = Operations()
        result = oper.filterOdd(subject_original)
        self.assertEqual(result, subject_ethalon)

    def test_negative(self):
        subject_original = range(-5, 5)
        subject_ethalon = [-5, -4, -3, -2, -1]
        oper = Operations()
        result = oper.filterNegative(subject_original)
        self.assertEqual(result, subject_ethalon)

if __name__ == "__main__":
    unittest.main()