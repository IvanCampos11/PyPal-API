from datetime import date
import pandas as pd
import sys
from pathlib import Path
sys.path.append('')
from pypal_api.exceptions import *

def list_to_column(dateframes, lists, name):
    newSeries = pd.Series(lists)
    dateframes[name] = newSeries
    return dateframes
