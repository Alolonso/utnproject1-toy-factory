from classes.adminClass import Admin
from classes.employeeClass import Employee
from classes.clientClass import Client

from functions.files import readFile
from functions.data import getUsers, getOrders
from functions.menus import mainMenu
from functions.inputs import loginInput

users = getUsers(Admin, Employee, Client)
orders = getOrders()
supplies = {'wood/metal': 0, 'paint': 0, 'nails/screws': 0}

suppliesFile = readFile('supplies.txt')
if suppliesFile:
  supplies = suppliesFile

while True:
  option = mainMenu()

  if option == '1':
    user = loginInput(users)
    if user:
      users, orders, supplies = user.menu(users, orders, supplies)
    else:
      print('ERROR: Usuario no encontrado o inválido...')

  elif option == '2':
    break