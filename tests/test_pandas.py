import os
import sys
from pathlib import Path
import datetime
import unittest
import pandas as pd
import numpy as np

sys.path.append('')
from pypal_api.pypal_pandas import listToColumn, nullReport, nullClean


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

        df = listToColumn(df, new_list, name)

        self.assertListEqual(df.columns.tolist(), df2.columns.tolist())
        self.assertListEqual(df.values.tolist(), df2.values.tolist())

    def test_null_report(self):
        headers = ['A', 'B', 'C']
        rows = [(np.nan,3,5), (2,np.nan,6)]
        df = pd.DataFrame(rows, columns=headers)
        correct_message = "There are 2 NaN values in your DataFrame."
        assertion_answer = nullReport(df)
        self.assertEqual(assertion_answer, correct_message)


if __name__ == "__main__":
    unittest.main()


