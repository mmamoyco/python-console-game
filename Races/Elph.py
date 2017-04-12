from enum import Enum

from Races.Mob import Mob


#Damage
class ElphSkills(Enum):
    STEALS_STAB = 10
    LUCENT_BEAM = 16


class Elph(Mob):

    def __init__(self):
        Mob.__init__(self)
        self.maxHealth = 80
        self.damage = 15
        self.health = 80
        self.race = "Elph"
        # self.goodPhrases = ["Hello stranger, nice to meet you", "Ready for combat"]
        # self.badPhrases = ["You shall not pass!", "Prepare yourself! Evil not stand against me", "It's our plannet!"]


    def setSkill(self, skill):
        if skill == ElphSkills.STEALS_STAB:
            self.skill = ElphSkills.STEALS_STAB
        elif skill == ElphSkills.LUCENT_BEAM:
            self.skill = ElphSkills.LUCENT_BEAM



    @staticmethod
    def showInfo():
        return "Elph is  REWIEW HERE\n" + \
                "ELPH race have two skills: \x1b[35;1;4mstealth stab\x1b[0m and \x1b[35;1;4mLucent beam\x1b[0m which gives a lot of damage to enermy"





