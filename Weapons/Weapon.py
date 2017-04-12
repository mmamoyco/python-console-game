
class Weapon():

    def __init__(self):
        self.damage = 1
        self.usage = 2
        self.price = 100

    # def __str__(self):
    #     return self.__class__.__name__

    def getDesription(self):
        return "WEAPON - " + self.__class__.__name__ + "\nDamage: " + str(self.damage) + "\nNumberOfUsage: " + str(self.usage) + \
               "\nPrice: " + str(self.price) +"\n\x1b[31;1m----------------\x1b[0m"

    def __str__(self):
        return "\x1b[31;1m" + self.__class__.__name__ + "\x1b[0m: " +  "Damage - " + str(self.damage) + " NumberOfUsage - " + str(self.usage)