import datetime
from classes.userClass import User
from classes.orderClass import Order
from functions.menus import clientMenu
from functions.inputs import orderInput
from functions.data import sendToFile

class Client(User):
  def __init__(self, id, fullname, birthdate, mail, password, usertype = 'client'):
    self.id = id
    self.fullname = fullname
    self.birthdate = datetime.datetime.strptime(birthdate, '%Y-%m-%d').date()
    self.mail = mail
    self.password = password
    self.usertype = usertype

  def menu(self, users, orders, supplies):
    while True:
      option = clientMenu(self.fullname)

      if option == '1':
        newOrder = orderInput(users, 'pending')
        orders.append(Order.fromDict(newOrder))
        sendToFile('orders.json', orders)

      elif option == '2':
        break
    return users, orders, supplies