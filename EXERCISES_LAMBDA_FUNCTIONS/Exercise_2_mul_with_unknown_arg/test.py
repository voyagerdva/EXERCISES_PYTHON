import unittest
from Exercise import Lam

class testLambda(unittest.TestCase):

    def test_multiple(self):
        ins = Lam()
        result = ins.mul(100)

        self.assertEqual(result(20),2000)
        self.assertEqual(result(30),3000)
        self.assertEqual(result(11),1100)


if __name__ == "__main__":
    unittest.main()