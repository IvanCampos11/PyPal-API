import os
import sys
from pathlib import Path
import datetime
import unittest
sys.path.append('')
from pypal_api.pypal_dates import *


class DatesTest(unittest.TestCase):
    """These test if the dates functions work correctly"""

    def test_dateToString(self):
        date_one = datetime.datetime(2021, 12, 1)
        date_two = datetime.datetime(2021, 11, 29)

        finished_date_one = dateToString(date_one)
        finished_date_two = dateToString(date_two)

        self.assertEqual(finished_date_one, "2021-12-01")
        self.assertEqual(type(finished_date_one), str)

        self.assertEqual(finished_date_two, "2021-11-29")
        self.assertEqual(type(finished_date_two), str)

    def test_newDate(self):
        test_day = 2
        output_one = "string"
        output_two = 'date'
        date_from = datetime.datetime(2021, 12, 1)

        test_one = newDate(test_day)
        answer_one = datetime.date.today() + datetime.timedelta(days=2)
        self.assertEqual(test_one, str(answer_one))

        test_two = newDate(test_day, return_type=output_two)
        answer_two = datetime.date.today() + datetime.timedelta(days=test_day)
        self.assertEqual(test_two, answer_two)

    def test_findDayName(self):
        dateOne = '2021-12-06'
        dateTwo = '2021-12-11'
        dateThree = '2021-12-12'

        self.assertEqual(findDayName(dateOne), 'Monday')
        self.assertEqual(findDayName(dateTwo), 'Saturday')
        self.assertEqual(findDayName(dateThree), 'Sunday')

        self.assertTrue(findDayName(dateThree, checkWeekend=True))
        self.assertFalse(findDayName(dateOne, checkWeekend=True))

    def test_date_validator(self):
        true_date_list = [
            "Sep 13, 2005",
            "March 30, 2010",
            "Jan 19,1990",
            "06/19/1860",
            "01/19/90",
            "2022",
            "Feb 1998",
            "January1990",
            "08-30-2000",
        ]

        false_date_list = [
            "Sep 40, 2005",
            "Pizza 30, 2010",
            "Jan bst,1990",
            "06/19=1860",
            "0l/19/90",
            "202s",
            "Ferb 1998",
            "Taco1990",
            "08?30?2000",
        ]

        for test_date in true_date_list:
            self.assertTrue(date_validator(test_date))
        for test_date in false_date_list:
            self.assertFalse(date_validator(test_date))

if __name__ == "__main__":
    unittest.main()
