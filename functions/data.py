from classes.orderClass import Order
from functions.files import readFile, writeFile

def objectListToArray(data):
  return [obj.toDict() for obj in data]

def getUsers(Admin, Employee, Client):
  users = []
  usersFile = readFile('users.json')
  if usersFile:
    for user in usersFile:
      if user['usertype'] == 'admin':
        users.append(Admin.fromDict(user))
      elif user['usertype'] == 'employee':
        users.append(Employee.fromDict(user))
      elif user['usertype'] == 'client':
        users.append(Client.fromDict(user))
  return users

def getOrders():
  orders = []
  ordersFile = readFile('orders.json')
  if ordersFile:
    for order in ordersFile:
      orders.append(Order.fromDict(order))
  return orders

def sendToFile(file, data):
  array = objectListToArray(data)
  writeFile(file, array)