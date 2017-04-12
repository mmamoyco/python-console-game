class Poison():

    def __init__(self):
        self.name = ""
        self.recoverCount = 0
        self.price = 0
        self.amount = 0

    def __str__(self):
        return "\x1b[31;1m"+self.name+"\x1b[0m recover " + str(self.recoverCount) + " points of "+self.name+"."

    def getDesription(self):
        return "\x1b[34;1m" + self.name + "\x1b[0m \nRecover: " + str(self.recoverCount) + "\nPrice: " + str(self.price) + \
              "\n\x1b[31;1m----------------\x1b[0m"