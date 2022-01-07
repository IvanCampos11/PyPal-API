import os
import sys
from pathlib import Path
import datetime
import unittest
import pandas as pd

sys.path.append('')
from pypal_api.pypal_pandas import list_to_column


class PandasTest(unittest.TestCase):


    def test_list_to_column(self):
        headers = ['A', 'B', 'C']
        headers2 = ['A', 'B', 'C', 'D']
        rows = [(1,3,5), (2,4,6)]
        rows2 = [(1,3,5,7), (2,4,6,8)]
        df = pd.DataFrame(rows, columns=headers)
        df2 = pd.DataFrame(rows2, columns=headers2)

        new_list = [7,8]
        name = 'D'

        df = list_to_column(df, new_list, name)

        self.assertListEqual(df.columns.tolist(), df2.columns.tolist())
        self.assertListEqual(df.values.tolist(), df2.values.tolist())

    def test_null_report(self):
        pass


if __name__ == "__main__":
    unittest.main()


