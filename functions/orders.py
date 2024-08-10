import datetime
from classes.userClass import User
from functions.menus import commandMenu
from functions.inputs import dateInput
from functions.data import sendToFile
from functions.files import writeFile

carNeeds = {
  'wood/metal': 4,
  'paint': 3,
  'nails/screws': 5
}

dollNeeds = {
  'wood/metal': 1,
  'paint': 5,
  'nails/screws': 2
}

ballNeeds = {
  'wood/metal': 8,
  'paint': 4,
  'nails/screws': 0
}

toys = {
  'car': 'Carro',
  'doll': 'Muñeca',
  'ball': 'Balón'
}

states = {
  'pending': 'En espera...',
  'approved': 'Aprobado',
  'completed': 'Completado'
}

def orderDetails(order, client, number):
  print(f'\nPedido: #{number}')
  print(f'Cliente: {client.id} - {client.fullname}')
  print(f'Juguete: {toys[order.toy]}')
  print(f'Fecha: {order.date}')
  print(f'Dirección: {order.address}')
  print(f'Estado: {states[order.state]}')

def readRequests(users, orders):
  for i, order in enumerate(orders):
    if order.state == 'pending':
      client = User.getUser(order.id, users)
      orderDetails(order, client, i + 1)
      option = commandMenu('nextExit')
      if option == 'd':
        continue
      elif option == 'q':
        break

def readTodayRequests(users, orders):
  today = datetime.datetime.now().date()
  for i, order in enumerate(orders):
    if order.date == today:
      client = User.getUser(order.id, users)
      orderDetails(order, client, i + 1)
      option = commandMenu('nextExit')
      if option == 'd':
        continue
      elif option == 'q':
        break

def readRequestsByDate(users, orders):
  date = dateInput()
  for i, order in enumerate(orders):
    if order.date == date:
      client = User.getUser(order.id, users)
      orderDetails(order, client, i + 1)
      option = commandMenu('nextExit')
      if option == 'd':
        continue
      elif option == 'q':
        break

def readOrders(users, orders):
  for i, order in enumerate(orders):
    if order.state == 'approved':
      client = User.getUser(order.id, users)
      orderDetails(order, client, i + 1)
      option = commandMenu('nextExit')
      if option == 'd':
        continue
      elif option == 'q':
        break

def readCompletedOrders(users, orders):
  for i, order in enumerate(orders):
    if order.state == 'completed':
      client = User.getUser(order.id, users)
      orderDetails(order, client, i + 1)
      option = commandMenu('nextExit')
      if option == 'd':
        continue
      elif option == 'q':
        break

def approveOrRejectRequests(users, orders):
  for i, order in enumerate(orders):
    if order.state == 'pending':
      client = User.getUser(order.id, users)
      orderDetails(order, client, i + 1)
      option = commandMenu('nextExitApproveReject')
      if option == 'd':
        continue
      elif option == 's':
        order.state = 'approved'
        sendToFile('orders.json', orders)
      elif option == 'a':
        orders.pop(i)
        sendToFile('orders.json', orders)
      elif option == 'q':
        return orders
  return orders

def rejectOrders(users, orders):
  for i, order in enumerate(orders):
    if order.state == 'approved':
      client = User.getUser(order.id, users)
      orderDetails(order, client, i + 1)
      option = commandMenu('nextExitReject')
      if option == 'd':
        continue
      elif option == 'a':
        orders.pop(i)
        sendToFile('orders.json', orders)
      elif option == 'q':
        return orders
  return orders

def processOrder(users, orders, supplies):
  toyNeeds = {
    'car': carNeeds,
    'doll': dollNeeds,
    'ball': ballNeeds
  }

  for i, order in enumerate(orders):
    if order.state == 'approved':
      client = User.getUser(order.id, users)
      orderDetails(order, client, i + 1)
      option = commandMenu('nextExitDevelop')
      if option == 'd':
        continue
      elif option == 'w':
        orderToyNeeds = toyNeeds[order.toy]
        available = True
        
        for key in orderToyNeeds:
          if orderToyNeeds[key] > supplies[key]:
            print('ERROR: Insumos insuficientes...')
            available = False

        if available == False:
          continue

        for key in orderToyNeeds:
          supplies[key] -= orderToyNeeds[key]

        order.state = 'completed'
        sendToFile('orders.json', orders)
        writeFile('supplies.txt', supplies)

      elif option == 'q':
        return orders, supplies
  return orders, supplies

def availableVsRequiredSupplies(orders, supplies):
  requiredSupplies = {'wood/metal': 0, 'paint': 0, 'nails/screws': 0}
  toSupply = {'wood/metal': 0, 'paint': 0, 'nails/screws': 0}
  toyNeeds = {
    'car': carNeeds,
    'doll': dollNeeds,
    'ball': ballNeeds
  }

  for order in orders:
    if order.state == 'approved':
      orderToyNeeds = toyNeeds[order.toy]
      for key in orderToyNeeds:
        requiredSupplies[key] += orderToyNeeds[key]
  
  print('\nINSUMOS DISPONIBLES')
  print(f'Madera/metal: {supplies["wood/metal"]}')
  print(f'Pintura: {supplies["paint"]}')
  print(f'Clavos/tornillos: {supplies["nails/screws"]}')

  print('\nINSUMOS REQUERIDOS')
  print(f'Madera/metal: {requiredSupplies["wood/metal"]}')
  print(f'Pintura: {requiredSupplies["paint"]}')
  print(f'Clavos/tornillos: {requiredSupplies["nails/screws"]}')

  for key in orderToyNeeds:
    if supplies[key] - requiredSupplies[key] < 0:
      toSupply[key] = requiredSupplies[key] - supplies[key]

  print('\nINSUMOS FALTANTES')
  print(f'Madera/metal: {toSupply["wood/metal"]}')
  print(f'Pintura: {toSupply["paint"]}')
  print(f'Clavos/tornillos: {toSupply["nails/screws"]}')

def finishedItems(orders):
  counter = 0
  for order in orders:
    if order.state == 'completed':
      counter += 1
  print(f'\nORDENES TERMINADAS: {counter}')