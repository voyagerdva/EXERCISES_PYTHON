import unittest
from Exercise import Operations



class testLambda(unittest.TestCase):

    def test_True(self):
        subject_ethalon = True
        oper = Operations()
        result = oper.findPrefix("Python")("Python")
        self.assertEqual(result, subject_ethalon)

    def test_False(self):
        subject_ethalon = False
        oper = Operations()
        result = oper.findPrefix("Java")("Java")
        self.assertEqual(result, subject_ethalon)


if __name__ == "__main__":
    unittest.main()