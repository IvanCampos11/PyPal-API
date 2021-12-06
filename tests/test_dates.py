import os
import sys
from pathlib import Path
import datetime
import unittest

file = Path(__file__). resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))
from pypal_api.pypal_dates import date_to_string, new_date


class DatesTest(unittest.TestCase):
    """These test if the dates functions work correctly"""

    def test_date_to_string(self):
        date_one = datetime.datetime(2021, 12, 1)
        date_two = datetime.datetime(2021, 11, 29)

        finished_date_one = date_to_string(date_one)
        finished_date_two = date_to_string(date_two)

        self.assertEqual(finished_date_one, "2021-12-01")
        self.assertEqual(type(finished_date_one), str)

        self.assertEqual(finished_date_two, "2021-11-29")
        self.assertEqual(type(finished_date_two), str)

    def test_new_date(self):
        test_day = 2
        output_one = "string"
        output_two = 'date'
        date_from = datetime.datetime(2021, 12, 1)

        test_one = new_date(test_day)
        answer_one = datetime.date.today() + datetime.timedelta(days=2)
        self.assertEqual(test_one, str(answer_one))

        test_two = new_date(test_day, return_type=output_two)
        answer_two = datetime.date.today() + datetime.timedelta(days=test_day)
        self.assertEqual(test_two, answer_two)


if __name__ == "__main__":
    unittest.main()
