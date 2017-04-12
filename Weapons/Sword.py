from Weapons.Weapon import Weapon

class Sword(Weapon):

    def __init__(self):
        Weapon.__init__(self)
        self.damage = 17
        self.usage = 1
        self.price = 550
        self.name = "Sword"