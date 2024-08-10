import datetime
from classes.userClass import User

def inputWithValidation(prompt, validationFunc, errorMessage):
  value = input(f'\n{prompt}')
  while not validationFunc(value):
    print(f'ERROR: {errorMessage}')
    value = input(prompt)
  return value

def validateId(id, data):
  return bool(id) and User.getUser(id, data) is None

def validateNumber(value):
  return bool(value) and value.isdigit()

def validateNotEmpty(value):
  return bool(value)

def validateYear(year):
  return year.isdigit() and len(year) == 4

def validateMonth(month):
    return month.isdigit() and 1 <= int(month) <= 12

def validateDay(day):
    return day.isdigit() and 1 <= int(day) <= 31

def validateDate(year, month, day):
  try:
    datetime.datetime(int(year), int(month), int(day))
    return True
  except:
    return False