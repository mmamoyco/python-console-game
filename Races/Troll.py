from enum import Enum

from Races.Mob import Mob


#Damage
class TrollSkills(Enum):
    RAGE = 25
    CANNIBALISM = 30


class Troll(Mob):

    def __init__(self):
        Mob.__init__(self)
        self.maxHealth = 160
        self.damage = 4
        self.health = 160
        self.race = "Troll"
        # self.goodPhrases = ["Hello stranger, nice to meet you", "Ready for combat"]
        # self.badPhrases = ["You shall not pass!", "Prepare yourself! Evil not stand against me", "It's our plannet!"]


    def setSkill(self, skill):
        if skill == TrollSkills.RAGE:
            self.skill = TrollSkills.RAGE
        elif skill == TrollSkills.CANNIBALISM:
            self.skill = TrollSkills.CANNIBALISM



    @staticmethod
    def showInfo():
        return "Troll is  REWIEW HERE\n" + \
                "Troll race have two skills: \x1b[34;1;4mRage\x1b[0m and \x1b[34;1;4mCannubalism\x1b[0m which gives a lot of damage to enermy"





