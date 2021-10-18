import unittest
from Exercise import listOperation as LO

class testLambda(unittest.TestCase):

    def test_multiple(self):
        subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        subject_ethalon = [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
        inst = LO()
        inst.listSort(subject_marks)
        self.assertEqual(subject_marks, subject_ethalon)

if __name__ == "__main__":
    unittest.main()