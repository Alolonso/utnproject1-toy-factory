def employeeMenu(employee):
  print(f'\nMENÚ EMPLEADO - {employee}')
  print('1. Registrar clientes')
  print('2. Realizar/Finalizar pedido')
  print('3. Leer completados')
  print('4. Abastecer insumos')
  print('5. Cerrar cesión')

  while True:
    option = input('Seleccione una opción: ')
    if option in {'1', '2', '3', '4', '5'}:
      return option
    else:
      print('ERROR: Opción inválida...')

def clientMenu(client):
  print(f'\nMENÚ CLIENTE - {client}')
  print('1. Crear pedido')
  print('2. Cerrar cesión')

  while True:
    option = input('Seleccione una opción: ')
    if option in {'1', '2'}:
      return option
    else:
      print('ERROR: Opción inválida...')

def adminMenu(admin):
  print(f'\nMENÚ ADMINISTRADOR - {admin}')
  print('1. Leer solicitudes')
  print('2. Aprobar/Rechazar solicitudes')
  print('3. Procesar pedidos')
  print('4. Consultas')
  print('5. Registrar empleados')
  print('6. Cerrar cesión')

  while True:
    option = input('Seleccione una opción: ')
    if option in {'1', '2', '3', '4', '5', '6'}:
      return option
    else:
      print('ERROR: Opción inválida...')

def requestMenu():
  print('\nOPCIONES DE SOLICITUDES')
  print('1. Ver todas las solicitudes')
  print('2. Ver solicitudes de hoy')
  print('3. Ver solicitudes de una fecha específica')
  print('4. Salir')

  while True:
    option = input('Seleccione una opción: ')
    if option in {'1', '2', '3', '4'}:
      return option
    else:
      print('ERROR: Opción inválida...')

def orderMenu():
  print('\nOPCIONES DE PEDIDOS')
  print('1. Leer pedidos')
  print('2. Rechazar pedidos')
  print('3. Crear pedido')
  print('4. Salir')

  while True:
    option = input('Seleccione una opción: ')
    if option in {'1', '2', '3', '4'}:
      return option
    else:
      print('ERROR: Opción inválida...')

def toyMenu():
  print('\nOPCIONES DE JUGUETES')
  print('1. Carro')
  print('2. Balón')
  print('3. Muñeca')

  while True:
    option = input('Seleccione una opción: ')
    if option == '1':
      return 'car'
    elif option == '2':
      return 'ball'
    elif option == '3':
      return 'doll'
    else:
      print('ERROR: Opción inválida...')

def queryMenu():
  print('\nOPCIONES DE CONSULTAS')
  print('1. Ver insumos requeridos vs disponibles')
  print('2. Ver artículos terminados')
  print('3. Salir')

  while True:
    option = input('Seleccione una opción: ')
    if option in {'1', '2', '3'}:
      return option
    else:
      print('ERROR: Opción inválida...')

def commandMenu(type):
  if type == 'nextExit':
    print('OPCIONES: Siguiente: D | Salir: Q')
    while True:
      option = input('Seleccione una opción: ').lower()
      if option in {'d', 'q'}:
        return option
      else:
        print('ERROR: Opción inválida...')

  elif type == 'nextExitApproveReject':
    print('Siguiente: D | Aprobar: S | Rechazar: A | Salir: Q')
    while True:
      option = input('Seleccione una opción: ').lower()
      if option in {'d', 's', 'a', 'q'}:
        return option
      else:
        print('ERROR: Opción inválida...')

  elif type == 'nextExitReject':
    print('Siguiente: D | Rechazar: A | Salir: Q')
    while True:
      option = input('Seleccione una opción: ').lower()
      if option in {'d', 'a', 'q'}:
        return option
      else:
        print('ERROR: Opción inválida...')

  elif type == 'nextExitDevelop':
    print('Siguiente: D | Desarrollar: W | Salir: Q')
    while True:
      option = input('Seleccione una opción: ').lower()
      if option in {'d', 'w', 'q'}:
        return option
      else:
        print('ERROR: Opción inválida...')

def mainMenu():
  print('\nMENÚ PRINCIPAL')
  print('1. Iniciar sesión')
  print('2. Salir')

  while True:
    option = input('Seleccione una opción: ')
    if option in {'1', '2'}:
      return option
    else:
      print('ERROR: Opción inválida...')

def suppliesMenu():
  print('\nMENÚ DE INSUMOS')
  print('1. Madera/metal')
  print('2. Pintura')
  print('3. Clavos/tornillos')
  print('4. Salir')

  while True:
    option = input('Seleccione una opción: ')
    if option in {'1', '2', '3', '4'}:
      return option
    else:
      print('ERROR: Opción inválida...')