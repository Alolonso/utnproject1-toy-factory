import datetime

class Order:
  def __init__(self, id, toy, date, address, state):
    self.id = id
    self.toy = toy
    self.date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    self.address = address
    self.state = state

  @classmethod
  def fromDict(cls, order):
    return cls(
      order['id'],
      order['toy'],
      order['date'],
      order['address'],
      order['state']
    )
    
  def toDict(self):
    return {
      'id': self.id,
      'toy': self.toy,
      'date': str(self.date),
      'address': self.address,
      'state': self.state
    }