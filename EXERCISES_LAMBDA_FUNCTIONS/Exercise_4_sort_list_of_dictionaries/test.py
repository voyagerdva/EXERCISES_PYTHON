import unittest
from Exercise import Lam



class testLambda(unittest.TestCase):

    def test_multiple(self):
        subject_marks = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
        subject_ethalon = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
        brands = Lam()
        result = brands.sortedList(subject_marks)
        self.assertEqual(result, subject_ethalon)

if __name__ == "__main__":
    unittest.main()