# **PyPal-API**

<p align="center">

<img src="https://img.shields.io/github/license/ivancampos11/PyPal-API" alt="License">

<img src="https://img.shields.io/github/repo-size/ivancampos11/PyPal-API" alt="Repo Size">

<img src="https://img.shields.io/github/last-commit/ivancampos11/PyPal-API" alt="Last Commit">

<img src="https://img.shields.io/github/commit-activity/m/ivancampos11/PyPal-API" alt="Commits a Month">

<img src="https://img.shields.io/github/pipenv/locked/python-version/ivancampos11/PyPal-API" alt="Supported Python versions">

<img src="https://img.shields.io/pypi/v/PyPal-API" alt="Current PyPi Version">

</p>

---

## What is it?
PyPal-API is a python package that includes helper functions that ease development of API's for the most popular API's (google,shopify,etc) and tools such as FastAPI and Flask.
There aren't a lot of content at the moment but given time, it will hopfully grow into a huge project helping countless number of people!

- date_to_string: very simple function that with an input of a datetime object, it will return the date as a string!

- new_date: Input a number (positive or negative) to tell this function the amount of days before or after the current day, default returned value is a string

---

## Getting Started

To get started using this package, install from test pypi here: 

https://test.pypi.org/project/pypal-api/

If you're really lazy you can use this PiP command to install it:

```bash
$ pip install -i https://test.pypi.org/simple/ pypal-api
```

---

## date_to_string
Simple function that you input a datetime and it will return it in the nice simple string format YYY-MM-DD

code to use: 

```python
from pipal_api import date_to_string
import datetime

date = datetime.datetime(2021,12,2)

date_to_string(date)
```

---

## new_date
Input a `number` (positive or negative) and it'll return (default: `string`. other options include `datetime` or `string`/`integer` list) the specified `return_type`. 
The default `from_date` uses `datetime.date.today()` but can use a `string` date (YYYY-MM-DD) or a `datetime` and it will act accordingly.

```python
from pipal_api import new_date

new_date(2)
```
