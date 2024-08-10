import datetime
from classes.userClass import User
from functions.validations import inputWithValidation, validateId, validateNotEmpty, validateYear, validateMonth, validateDay, validateDate, validateNumber
from functions.menus import toyMenu

def userInput(data):
  id = inputWithValidation(
    'Ingrese la cédula: ',
    lambda x: validateId(x, data),
    'Usuario no encontrado o inválido...'
  )

  fullname = inputWithValidation(
    'Ingrese el nombre completo: ',
    validateNotEmpty,
    'El nombre no puede estar vacío...'
  )

  print('Fecha de nacimiento...')
  year = inputWithValidation(
    'Ingrese el año (YYYY): ',
    validateYear,
    'Año inválido...'
  )
  month = inputWithValidation(
    'Ingrese el mes (MM): ',
    validateMonth,
    'Mes inválido...'
  )
  day = inputWithValidation(
    'Ingrese el día (DD): ',
    validateDay,
    'Día inválido...'
  )
  if not validateDate(year, month, day):
    print('ERROR: Fecha inválida...')
    return
  date = datetime.datetime(int(year), int(month), int(day))

  mail = inputWithValidation(
    'Ingrese el correo electrónico: ',
    validateNotEmpty,
    'El correo electrónico no puede estar vacío...'
  )

  password = inputWithValidation(
    'Ingrese la contraseña: ',
    validateNotEmpty,
    'La contraseña no puede estar vacía...'
  )

  return {
    'id': id,
    'fullname': fullname,
    'birthdate': str(date.date()),
    'mail': mail,
    'password': password
  }

def orderInput(data, state):
  id = inputWithValidation(
    'Ingrese la cédula: ',
    lambda x: User.getUser(x, data) and User.getUser(x, data).usertype == 'client',
    'Usuario no encontrado o inválido...'
  )

  client = User.getUser(id, data)

  toy = toyMenu()

  address = inputWithValidation(
    'Indique la dirección del pedido: ',
    validateNotEmpty,
    'La dirección no puede estar vacía...'
  )

  return {
    'id': client.id,
    'toy': toy,
    'date': str(datetime.datetime.now().date()),
    'address': address,
    'state': state
  }

def dateInput():
  year = inputWithValidation(
    'Ingrese el año (YYYY): ',
    validateYear,
    'Año inválido...'
  )
  month = inputWithValidation(
    'Ingrese el mes (MM): ',
    validateMonth,
    'Mes inválido...'
  )
  day = inputWithValidation(
    'Ingrese el día (DD): ',
    validateDay,
    'Día inválido...'
  )
  if not validateDate(year, month, day):
    print('ERROR: Fecha inválida...')
    return
  return datetime.datetime(int(year), int(month), int(day)).date()

def loginInput(data):
  print('\nLOGIN')
  id = input('Ingrese la cédula: ')
  password = input('Ingrese la contraseña: ')

  user = User.getUser(id, data)
  if user:
    if user.password == password:
      return user
    else:
      return None

def suppliesInput(supply):
  value = inputWithValidation(
    f'Ingrese la cantidad de {supply} que deseas ingresar: ',
    validateNumber,
    'Valor inválido...'
  )

  return int(value)