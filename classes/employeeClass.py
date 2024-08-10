import datetime
from classes.userClass import User
from classes.clientClass import Client
from functions.menus import employeeMenu, suppliesMenu
from functions.inputs import userInput, suppliesInput
from functions.data import sendToFile, writeFile
from functions.orders import processOrder, readCompletedOrders

class Employee(User):
  def __init__(self, id, fullname, birthdate, mail, password, usertype = 'employee'):
    self.id = id
    self.fullname = fullname
    self.birthdate = datetime.datetime.strptime(birthdate, '%Y-%m-%d').date()
    self.mail = mail
    self.password = password
    self.usertype = usertype

  def menu(self, users, orders, supplies):
    while True:
      option = employeeMenu(self.fullname)
      if option == '1':
        newUser = userInput(users)
        users.append(Client.fromDict(newUser))
        sendToFile('users.json', users)

      elif option == '2':
        orders, supplies = processOrder(users, orders, supplies)

      elif option == '3':
        readCompletedOrders(users, orders)

      elif option == '4':
        print()
        while True:
          option = suppliesMenu()
          if option == '1':
            value = suppliesInput('madera/metal')
            supplies['wood/metal'] += value
          elif option == '2':
            suppliesInput('pintura')
            supplies['paint'] += value
          elif option == '3':
            suppliesInput('clavos/tornillos')
            supplies['nails/screws'] += value
          elif option == '4':
            break
        writeFile('supplies.txt', supplies)

      elif option == '5':
        return users, orders, supplies