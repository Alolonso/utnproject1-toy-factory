class User:
  @classmethod
  def fromDict(cls, user):
    return cls(
      user['id'],
      user['fullname'],
      user['birthdate'],
      user['mail'],
      user['password']
    )
    
  def toDict(self):
    return {
      'id': self.id,
      'fullname': self.fullname,
      'birthdate': str(self.birthdate),
      'mail': self.mail,
      'password': self.password,
      'usertype': self.usertype
    }
  
  def getUser(id, data):
    for user in data:
      if user.id == id:
        return user
    return None