from datetime import datetime, timedelta
from datetime import timedelta, date
from os import error
import sys
from pathlib import Path
import calendar
sys.path.append('')
from pypal_api.exceptions import *


def dateToString(date_input):
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
    if " " in str(date):
        new_date = str(date_input).split(" ")
        return new_date[0]
    else:
        return str(date_input)


def findDayName(date: str, checkWeekend=False):
    """
    Input a date (string or datetime) and the returned data is the day name.
    If weekend = True, it will return True or False if the name is Saturday or Sunday.

    ----------
    Parameters
    ----------
    date : Datetime or String
    weekend : Boolean

    -------
    Returns
    -------
    String unless weekend = True, then it's a Boolean
    """

    date = dateToString(date)

    year, month, day = (int(i) for i in date.split('-'))
    dayNumber = calendar.weekday(year, month, day)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]
    if checkWeekend == False:
        return days[dayNumber]
    elif checkWeekend == True:
        if dayNumber == 5 or dayNumber == 6:
            return True
        else:
            return False
    else:
        error_message = f"""
            {checkWeekend} is not a valid input! Required(Bool, True or False)
            """
        raise InvalidInputError(error_message)


def newDate(num_days: int, from_date=date.today(), return_type='string', weekends=True, weekdays=True):
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

    type_errors = {
        num_days: [int, 'Integer'],
        weekends: [bool, 'Boolean'],
        weekdays: [bool, 'Boolean'],
        return_type: [str, 'String'],
        from_date: [str, 'String']
    }

    for type_name, content_list in type_errors.items():
        if type(type_name) != content_list[0]:
            error_message = f"""
            {num_days} isn't a valid input! Required ({content_list[1]})
            """

    if '-' not in str(from_date):
        error_message = f"""
            {from_date} is not a valid input! Required(Datetime or String(YYYY-MM-DD))
            """
        raise InvalidInputError(error_message)
    if type(from_date) == str:
        split_date = from_date.split('-')
        if split_date[2].startswith('0'):
            split_date[2] = split_date[2][1:]
        from_date = datetime(int(split_date[0]), int(
            split_date[1]), int(split_date[2]))

    types = {
        "string": ['str', 'string'],
        "date": ['date', 'datetime', 'date time'],
        "integer list": ['int list', 'integer list', 'int-list', 'integer-list', 'int-lst', 'integer-lst'],
        "string list": ['str list', 'string list', 'str-list', 'string-list', 'str-lst', 'string-lst'],
        'list': ['lst', 'list']
    }

    day_types = {'weekends': ['Saturday', 'Sunday'], 'weekdays': [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]}

    count_days = 0
    num_of_days = 0
    day = date.today()
    if str(num_days).startswith('-'):
        num_days = int(str(num_days)[1:])
        if weekdays == False and weekends == False:
            error_message = f"""
            Both weekends and weekdays cannot be False!
            """
            raise InvalidInputError(error_message)
        elif weekends == False:
            while count_days < num_days:
                day = day - timedelta(days=1)
                if findDayName(str(day)) not in day_types['weekends']:
                    count_days += 1
                num_of_days += 1

            new_created_date = from_date - timedelta(days=num_of_days)
        elif weekdays == False:
            while count_days < num_days:
                day = day - timedelta(days=1)
                if findDayName(str(day)) not in day_types['weekdays']:
                    count_days += 1
                num_of_days += 1
            new_created_date = from_date - timedelta(days=num_of_days)
        else:
            new_created_date = from_date - timedelta(days=num_days)
    else:
        if weekdays == False and weekends == False:
            error_message = f"""
            Both weekends and weekdays cannot be False!
            """
            raise InvalidInputError(error_message)
        elif weekends == False:
            while count_days < num_days:
                day = day + timedelta(days=1)
                if findDayName(str(day)) not in day_types['weekends']:
                    count_days += 1
                num_of_days += 1
            new_created_date = from_date + timedelta(days=num_of_days)
        elif weekdays == False:
            while count_days < num_days:
                day = day + timedelta(days=1)
                if findDayName(str(day)) not in day_types['weekdays']:
                    count_days += 1
                num_of_days += 1
            new_created_date = from_date + timedelta(days=num_of_days)
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
        new_created_date = dateToString(new_created_date)
        return new_created_date
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
        new_created_date = dateToString(new_created_date)
        return new_created_date.split('-')
