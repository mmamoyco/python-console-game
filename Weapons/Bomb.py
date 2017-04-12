from Weapons.Weapon import Weapon

class Bomb(Weapon):

    def __init__(self):
        Weapon.__init__(self)
        self.damage = 50
        self.usage = 1
        self.price = 1000
        self.name = "bomb"