from enum import Enum

from Races.Mob import Mob


#Damage
class HumanSkills(Enum):
    STRONG_HAND_ATTACK = 10
    HANDMADE_GRENADE = 22


class Human(Mob):

    def __init__(self):
        Mob.__init__(self)
        self.maxHealth = 100
        self.damage = 7
        self.race = "Human"
        self.goodPhrases = ["Hello stranger, nice to meet you", "Ready for combat"]
        self.badPhrases = ["You shall not pass!", "Prepare yourself! Evil not stand against me", "It's our plannet!"]




    def setSkill(self, skill):
        if skill == HumanSkills.STRONG_HAND_ATTACK:
            self.skill = HumanSkills.STRONG_HAND_ATTACK
        elif skill == HumanSkills.HANDMADE_GRENADE:
            self.skill = HumanSkills.HANDMADE_GRENADE



    @staticmethod
    def showInfo():
        return "Human is the core race that have good amount of damage + good health stats \n" + \
                "Human race have two skills: \x1b[31;1;4mstrong hand attack\x1b[0m and \x1b[31;1;4mhandmade grenade\x1b[0m which gives a lot of damage to enemy"



