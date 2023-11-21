from main import difficulty, health

global difficulty, health

class Levels:
  @classmethod
  def __init__(cls):
    super().__init__()

  @classmethod
  def SetHealth(cls):
    if difficulty == 1:
      health = 1000000
      return health > 100000
    elif difficulty == 2:
      health == 100000
      return health > 1000
    elif difficulty == 3:
      health = 1000
      return health > 100
    elif difficulty == 8:
      health = 1000
      return health > 100
    elif difficulty == 9:
      health = 100
      return health >10

  @classmethod
  def UpdateHealth(cls, ammt: int):
    health += ammt
    return health > 1
