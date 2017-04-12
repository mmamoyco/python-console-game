from Poisons.Poison import Poison
class ManaBottle(Poison):

    def __init__(self):
        self.name = "Mana"
        self.recoverCount = 50
        self.price = 200
        self.amount = 1

    # def __str__(self):
    #     return "\x1b[34;1mMana bottle\x1b[0m recover " + str(self.recoverCount) + " points of mana."

    # def getDesription(self):
    #     return  "\x1b[31;1mMana bottle\x1b[0m \nRecover: " + str(self.recoverCount) + "\nPrice: " + str(self.price) +\
    #            "\n\x1b[31;1m----------------\x1b[0m"