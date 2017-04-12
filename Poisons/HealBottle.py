from Poisons.Poison import Poison

class HealBottle(Poison):

    def __init__(self):
        self.name = "Health"
        self.recoverCount = 50
        self.price = 400
        self.amount = 1

    # def __str__(self):
    #     return "\x1b[31;1m"+self.__class__.__name__+"\x1b[0m recover " + str(self.recoverCount) + " points of health."

    # def getDesription(self):
    #     return "\x1b[34;1mHeal bottle\x1b[0m \nRecover: " + str(self.recoverCount) + "\nPrice: " + str(self.price) + \
    #            "\n\x1b[31;1m----------------\x1b[0m"