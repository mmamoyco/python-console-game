from Weapons.Weapon import Weapon

class Knife(Weapon):

    def __init__(self):
        Weapon.__init__(self)
        self.damage = 9
        #number of weapon usage
        self.usage = 3
        self.price = 300
        self.name = "knife"