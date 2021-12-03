import os
import sys
from pathlib import Path
import datetime
import unittest

file = Path(__file__). resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))
from pypal_api.pandas import list_to_column

class PandasTest(unittest.TestCase):


    def test_list_to_column(self):
        pass
