from datetime import date
import pandas as pd
import sys
from pathlib import Path
sys.path.append('')
from pypal_api.exceptions import *

def listToColumn(dateframes, lists, name):
    newSeries = pd.Series(lists)
    dateframes[name] = newSeries
    return dateframes

def nullReport(dataframe):
    nullFound = dataframe.isnull().sum().sum()
    if (nullFound == 1):
        answer1 = print('There is only', nullFound,
                        'NaN value in your DataFrame!')
        return answer1
    elif (nullFound > 1):
        answer2 = print('There are', nullFound,
                        'NaN values in your DataFrame.')
        return answer2
    else:
        print('There are no NaN values in your DataFrame!')
