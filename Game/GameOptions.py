from enum import Enum
from random import choice as random

from Game.View import View
from Races.Elph import Elph
from Races.Elph import ElphSkills
from Races.Human import Human
from Races.Human import HumanSkills
from Races.Troll import Troll
from Races.Troll import TrollSkills
from Weapons.Bomb import Bomb
from Weapons.Gun import Gun
from Weapons.Knife import Knife
from Weapons.Sword import Sword


class Race(Enum):
    HUMAN = 1
    TROLL = 2
    ELPH = 3


class GameOptions:
    def __init__(self):
        self.__gameView = View()
        self.__userNickName = self.__chooseNickName()
        self.__hero = self.__setUserHero(self.__chooseRace())
        self.__enemy = self.__generateEnermy()


    def __generateEnermy(self):
        weapons = [Bomb(), Sword(), Knife(), Gun(), None]
        randomedWeapon = random(weapons)
        enermies = []
        for race in Race:
            enermies.append(race)
        hero = random(enermies)

        if hero == Race.HUMAN:
            skills = []
            HERO =  Human()
            for skill in HumanSkills:
                skills.append(skill)
            HERO.skill = random(skills)

        elif hero == Race.ELPH:
            skills = []
            HERO = Elph()
            for skill in ElphSkills:
                skills.append(skill)
            HERO.skill = random(skills)

        elif hero == Race.TROLL:
            skills = []
            HERO = Troll()
            for skill in TrollSkills:
                skills.append(skill)
            HERO.skill = random(skills)

        HERO.weapon = randomedWeapon

        return HERO



    # Choose user race
    def __chooseRace(self):
        self.__gameView.show("Choose Race:")
        self.__gameView.show("1.\x1b[31;1m Human \x1b[0m")
        self.__gameView.show(Human.showInfo())
        self.__gameView.show("2.\x1b[34;1m Troll \x1b[0m")
        self.__gameView.show(Troll.showInfo())
        self.__gameView.show("3.\x1b[35;1m Elph \x1b[0m")
        self.__gameView.show(Elph.showInfo())

        userInput = self.__gameView.input()

        for race in Race:
            if race.value == int(userInput):
                return race


    # set userHero
    def __setUserHero(self, race):
        hero = None
        choice = self.__gameView.input("Choose skill. 1,2")
        if (race == race.HUMAN):
            hero = Human()
            # choice = self.__gameView.gameInput("Choose skill. 1,2")
            if int(choice) == 1:
                hero.setSkill(HumanSkills.STRONG_HAND_ATTACK)
            elif int(choice) == 2:
                hero.setSkill(HumanSkills.HANDMADE_GRENADE)
        elif race == race.ELPH:
            hero = Elph()
            # choice = input("Choose skill. 1,2")
            if int(choice) == 1:
                hero.setSkill(ElphSkills.STEALS_STAB)
            elif int(choice) == 2:
                hero.setSkill(ElphSkills.LUCENT_BEAM)
        elif race == race.TROLL:
            hero = Troll()
            # choice = input("Choose skill. 1,2")
            if int(choice) == 1:
                hero.setSkill(TrollSkills.RAGE)
            elif int(choice) == 2:
                hero.setSkill(TrollSkills.CANNIBALISM)
        return hero

    # enter nickname
    def __chooseNickName(self):
        return input("Enter hero name (Your nickname) ")
