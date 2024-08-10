import datetime
from classes.userClass import User
from classes.orderClass import Order
from classes.employeeClass import Employee
from functions.menus import adminMenu, requestMenu, orderMenu, queryMenu
from functions.orders import readRequests, readTodayRequests, readRequestsByDate, readOrders, approveOrRejectRequests, rejectOrders, availableVsRequiredSupplies, finishedItems
from functions.inputs import userInput, orderInput
from functions.data import sendToFile

class Admin(User):
  def __init__(self, id, fullname, birthdate, mail, password, usertype = 'admin'):
    self.id = id
    self.fullname = fullname
    self.birthdate = datetime.datetime.strptime(birthdate, '%Y-%m-%d').date()
    self.mail = mail
    self.password = password
    self.usertype = usertype

  def menu(self, users, orders, supplies):
    while True:
      option = adminMenu(self.fullname)

      if option == '1':
        while True:
          option = requestMenu()
          if option == '1':
            readRequests(users, orders)
          elif option == '2':
            readTodayRequests(users, orders)
          elif option == '3':
            readRequestsByDate(users, orders)
          elif option == '4':
            break

      elif option == '2':
        orders = approveOrRejectRequests(users, orders)

      elif option == '3':
        while True:
          option = orderMenu()
          if option == '1':
            readOrders(users, orders)
          elif option == '2':
            orders = rejectOrders(users, orders)
          elif option == '3':
            newOrder = orderInput(users, 'pending')
            orders.append(Order.fromDict(newOrder))
            sendToFile('orders.json', orders)
          elif option == '4':
            break

      elif option == '4':
        while True:
          option = queryMenu()
          if option == '1':
            availableVsRequiredSupplies(orders, supplies)
          elif option == '2':
            finishedItems(orders)
          elif option == '3':
            break

      elif option == '5':
        newUser = userInput(users)
        users.append(Employee.fromDict(newUser))
        sendToFile('users.json', users)

      elif option == '6':
        return users, orders, supplies