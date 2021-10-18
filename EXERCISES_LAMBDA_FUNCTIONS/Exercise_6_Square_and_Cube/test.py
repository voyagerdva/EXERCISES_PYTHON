import unittest
from Exercise import Operations



class testLambda(unittest.TestCase):
    # def __init__(self):
    #     self.subject_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_square(self):
        subject_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        subject_ethalon = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        oper = Operations()
        result = oper.squareNums(subject_original)
        self.assertEqual(result, subject_ethalon)

    def test_cube(self):
        subject_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        subject_ethalon = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
        oper = Operations()
        result = oper.cubeNums(subject_original)
        self.assertEqual(result, subject_ethalon)

if __name__ == "__main__":
    unittest.main()
