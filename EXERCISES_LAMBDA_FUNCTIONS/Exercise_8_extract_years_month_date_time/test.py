import unittest
from Exercise import Operations
import datetime

class testLambda(unittest.TestCase):

    def test_Year(self):
        subject_ethalon = 2021
        oper = Operations()
        now = datetime.datetime.now()
        result = oper.extractYear()(now)
        self.assertEqual(result, subject_ethalon)

    def test_Month(self):
        subject_ethalon = 8
        oper = Operations()
        now = datetime.datetime.now()
        result = oper.extractMonth()(now)
        self.assertEqual(result, subject_ethalon)

    def test_Day(self):
        subject_ethalon = 16
        oper = Operations()
        now = datetime.datetime.now()
        result = oper.extractDay()(now)
        self.assertEqual(result, subject_ethalon)

if __name__ == "__main__":
    unittest.main()

    #
    # class Operations():
    #     def extractYear(self):
    #         return lambda x: x.year
    #
    #     def extractMonth(self):
    #         return lambda x: x.month
    #
    #     def extractDay(self):
    #         return lambda x: x.day
    #
    #     def extractTime(self):
    #         return lambda x: x.time()
    #
    #
    # oper = Operations()
    # now = datetime.datetime.now()
    #
    # print(now)
    #
    # year = oper.extractYear()(now)
    # print(year)
    # month = oper.extractMonth()(now)
    # print(month)
    # day = oper.extractDay()(now)
    # print(day)
    # time = oper.extractTime()(now)
    # print(time)