import unittest
from Exercise import Lam

class testLambda(unittest.TestCase):

    def test_summ_0(self):
        r = Lam(0)
        self.assertEqual(r.summ()(0),0)
        self.assertEqual(r.summ()(10),10)
        self.assertEqual(r.summ()(20),20)

    def test_summ_10(self):
        r = Lam(10)
        self.assertEqual(r.summ()(10),20)
        self.assertEqual(r.summ()(100),110)

    def test_multiple(self):
        r = Lam(10)
        self.assertEqual(r.multiple()(10,20),200)
        self.assertEqual(r.multiple()(1,7),7)
        self.assertEqual(r.multiple()(100,20),2000)


if __name__ == "__main__":
    unittest.main()