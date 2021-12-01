import os, sys

import sys  
from pathlib import Path
file = Path(__file__). resolve()  
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))
import datetime
import unittest
from pypal_api.dates import date_to_string


class DatesTest(unittest.TestCase):
    """These test if the dates functions work correctly"""

    def test_dates(self):
        date_one = datetime.datetime(2021, 12,1)
        date_two = datetime.datetime(2021,11,29)

        finished_date_one = date_to_string(date_one)
        finished_date_two = date_to_string(date_two)

        self.assertEqual(finished_date_one, "2021-12-01")
        self.assertEqual(type(finished_date_one), str)

        self.assertEqual(finished_date_two, "2021-11-29")
        self.assertEqual(type(finished_date_two), str)

if __name__ == "__main__":
    unittest.main()