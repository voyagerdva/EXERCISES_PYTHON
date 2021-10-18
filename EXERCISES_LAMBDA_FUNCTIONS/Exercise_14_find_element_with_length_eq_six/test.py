import unittest
from Exercise import Operations

class testLambda(unittest.TestCase):
    def test_length6(self):
        original = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        ethalon = ['Monday', 'Friday', 'Sunday']
        fi = Operations()
        result = fi.find_six(original)
        self.assertEqual(result, ethalon)

if __name__ == "__main__":
    unittest.main()
