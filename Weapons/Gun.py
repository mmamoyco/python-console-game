from Weapons.Weapon import Weapon

class Gun(Weapon):

    def __init__(self):
        Weapon.__init__(self)
        self.damage = 40
        self.usage = 1
        self.price = 800
        self.name = "gun"

