from pypal_api.errors import InvalidInputError
from datetime import timedelta
from datetime import timedelta, date
import sys
from pathlib import Path

file = Path(__file__). resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))


def date_to_string(date_input):
    """
    Input a datetime object and it'll return in a nice and neat string

    ----------
    Parameters
    ----------
    date_input: Datetime

    -------
    Returns
    -------
    String
    """
    new_date = str(date_input).split(" ")
    return new_date[0]


def new_date(num_days, from_date=date.today(), return_type='string', weekends=True, weekdays=True):
    """
    Enter the number of days either ahead or behind, the returned data will be the correct date
    in the specified format (default str)

    ----------
    Parameters
    ----------
    num_days : Integer
    from_date : Date, String, or Integer
    type : Date, String, or Integer
    weekends : Boolean
    weekdays : Boolean

    -------
    Returns
    -------
    String
    """



    
    if type(num_days) != int:
        error_message = f"""
        '{num_days}' isn't a valid input! Required (Integer)
        """
        raise InvalidInputError(error_message)
    if type(weekends) != bool:
        error_message = f"""
        '{num_days}' isn't a valid input! Required (Boolean)
        """
        raise InvalidInputError(error_message)
    if type(weekdays) != bool:
        error_message = f"""
        '{num_days}' isn't a valid input! Required (Boolean)
        """
        raise InvalidInputError(error_message)
    if type(return_type) != str:
        error_message = f"""
        '{num_days}' isn't a valid input! Required (String)
        """
        raise InvalidInputError(error_message)

    types = {
        "string": ['str', 'string'],
        "date": ['date', 'datetime', 'date time'],
        "integer list": ['int list', 'integer list', 'int-list', 'integer-list', 'int-lst', 'integer-lst'],
        "string list": ['str list', 'string list', 'str-list', 'string-list', 'str-lst', 'string-lst'],
        'list': ['lst', 'list']
    }
    if str(num_days).startswith('-'):
        num_days = int(str(num_days)[1:])
        new_created_date = from_date - timedelta(days=num_days)
    else:
        new_created_date = from_date + timedelta(days=num_days)

    for key, value in types.items():
        if return_type.lower() in value:
            edited_return_type = key
            break
        else:
            edited_return_type = ''

    if edited_return_type == '':
        error_message = f"""
        "{return_type}" cannot be used as a type. Options (integer-list, string-list, string, date)
        """
        raise InvalidInputError(error_message)

    elif edited_return_type == 'string':
        return str(new_created_date)
    elif edited_return_type == 'date':
        return new_created_date
    elif edited_return_type == 'integer list' or edited_return_type == 'list':
        string_list = str(new_created_date).split("-")
        new_created_date = []
        for number in string_list:
            if number.startswith('0'):
                number = number[1:]
            new_created_date.append(int(number))
        return new_created_date
    elif edited_return_type == 'string list':
        return str(new_created_date).split("-")
