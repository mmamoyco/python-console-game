from Poisons.HealBottle import HealBottle
from Poisons.ManaBottle import ManaBottle

class Mob:

    def __init__(self):
        self.inventory = [HealBottle(),HealBottle(),  ManaBottle()]
        self.health = 100
        self.maxHealth = 100
        self.mana = 100
        self.maxMana = 100
        self.skill = None
        self.weapon = None

    def takeDamage(self, damage, cause):
        print(cause)
        self.health = self.health - damage


    def heal(self, numberOfhealth, cause):
        print(cause)
        if self.health + numberOfhealth > self.maxHealth:
            self.health = self.maxHealth
        else:
            self.health += numberOfhealth


    def addMana(self, numberOfMana, cause):
        print(cause)
        if self.mana + numberOfMana > self.maxMana:
            self.mana = self.mana
        else:
            self.health += numberOfMana


    def addInventoryItem(self, item):
        try:
            print(item + " added to inventory.")
        except TypeError:
            print(item.__str__() + " added to inventory.")
        finally:
            self.inventory.append(item)


    def removeInventoryItem(self, item):
        for element in self.inventory:
            if isinstance(element, type(item)):
                self.inventory.remove(element)

    def __str__(self):
        return "Race: " + self.__class__.__name__ + "\n" +\
               "Damage: " + str(self.damage) + "\n" + \
               "Health: " + str(self.health) + "\n" + \
               "Mana: " + str(self.mana) + "\n" + \
                "Speical Skill: " + str(self.skill)