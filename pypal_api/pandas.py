from datetime import date
import pandas as pd
import sys
from pathlib import Path

file = Path(__file__). resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

from pypal_api.errors import InvalidInputError

def list_to_column(dateframe, lists, name):
    newSeries = pd.Series(lists)
    dateframe[name] = newSeries
    return dateframe