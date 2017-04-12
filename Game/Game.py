import random
import time
from enum import Enum

from View import View
from Game.GameOptions import GameOptions
from Poisons.HealBottle import HealBottle
from Poisons.ManaBottle import ManaBottle
from Weapons.Bomb import Bomb
from Weapons.Gun import Gun
from Weapons.Knife import Knife
from Weapons.Sword import Sword
from Weapons.Weapon import Weapon


class Mode(Enum):
    OUT = 1
    INGAME = 2


class Game:


    def __init__(self):
        self.__heroCooldown = 0
        self.__enemyCooldown = 0
        self.__options = GameOptions()

        self.__gameView = View()

        self.__heroMoney = 1000
        self.__goods = [Sword(), Knife(), Gun(), Bomb(), HealBottle(), ManaBottle()]

    def __shop(self):
        self.gameView.show("\n\x1b[32;1m      WELCOME TO SHOP\x1b[0m \n \n\x1b[32;1m--------------------------\x1b[0m \n")
        exit = False
        while not exit:
            goodCounter = 1
            self.gameView.show("\n\x1b[30;1m              YOUR MONEY - " + str(self.heroMoney) + "\x1b[0m")
            for good in self.goods:
                self.gameView.show(str(goodCounter)+")")
                self.gameView.show(good.getDesription())
                goodCounter += 1
            self.gameView.show("\nTO EXIT SHOP ENTER 0")
            choice = self.gameView.input()
            if int(choice) == 0:
                exit = True
            else:
                choosedItem = self.goods[int(choice)-1]
                if self.heroMoney - choosedItem.price < 0:
                    self.gameView.show("NOT ENOGH MONEY! ")
                    time.sleep(2)
                    exit = True
                else:
                    if isinstance(choosedItem, Weapon):
                        self.options.hero.weapon = choosedItem

                    self.heroMoney = self.heroMoney - choosedItem.price
                    self.options.hero.addInventoryItem(self.goods[int(choice)-1])
                    self.goods.remove(self.goods[int(choice)-1])



    def __showStats(self, mode):
        if mode == Mode.OUT:
            self.gameView.show("\n\x1b[35;1m          " + self.options.userNickName + "\x1b[0m")
            self.gameView.show("\x1b[30;1mBalance: " + str(self.heroMoney) + "\x1b[0m")
            self.gameView.show(self.options.hero.__str__() + "\n\n")
        else:
            self.gameView.show("  \n\x1b[34;1m YOU\x1b[0m" + "                                                                       \x1b[31;1mENEMY\x1b[0m\n"
            "Race: " + self.options.hero.race + "                                                               Race: "+ self.options.enemy.race + "\n"
            "Damage: " + str(self.options.hero.damage) + "                                                                 Damage: " + str(self.options.enemy.damage) + "\n"
            "Health: " + str(self.options.hero.health) + "                                                               Health: " + str(self.options.enemy.health) + "\n"
            "Mana: " + str(self.options.hero.mana) + "                                                                 Mana: " + str(self.options.enemy.mana) + "\n"
            "Special Skills: " + str(self.options.hero.skill.name) + "                                                    ");
            # self.gameView.show(self.options.hero.__str__() + "\n")
            # self.gameView.show(self.options.enemy.__str__() + "\n\n")



    def __showInventory(self):
        self.gameView.show("\n\x1b[36;1m        YOUR INVENTORY \x1b[0m")
        for item in self.options.hero.inventory:
            print(item.__str__())
        self.gameView.show("\n")



    def startScenario(self):
        terminated = False
        while not terminated:
            self.gameView.show("1. SHOW MY STATS \n2. ENTER SHOP \n3. SHOW MY INVENTORY \n4. START BATTLE")
            choice = self.gameView.input()
            if int(choice) == 1:
                self.showStats(Mode.OUT)
            elif int(choice) == 2:
                self.shop()
            elif int(choice) == 3:
                self.showInventory()
            elif int(choice) == 4:
                self.startBattle()
                terminated = True


    def __startBattle(self):
        someoneDead = False
        while not someoneDead:
            dead = self.heroTurn()
            if dead == "hero":
                self.gameView.show("DEFEAT. YOU HERO DEAD")
                someoneDead = True
                break
            elif dead == "enemy":
                self.gameView.show("VICTORY!")
                someoneDead = True
                break
            dead = self.enemyTurn()
            if dead == "hero":
                self.gameView.show("DEFEAT. YOU HERO DEAD")
                someoneDead = True
                break
            elif dead == "enemy":
                self.gameView.show("VICTORY!")
                someoneDead = True
                break


    def __heroTurn(self):
        haveWeapon = False
        manaBottle = None
        healthBottle = None
        cooldown = False
        cooldownBreak = True
        numberOfHeal = 0
        numberOfMana = 0
        for element in self.options.hero.inventory:
            if not isinstance(element, Weapon):
                if element.price == 400:
                    numberOfHeal += 1
                    healthBottle = element
                else:
                    numberOfMana += 1
                    manaBottle = element
            else:
                haveWeapon = True

        # self.gameView.show("\n\n\n\n\n\n\YOUR ENEMY \n" + self.options.enemy.__str__())
        cooldownBreak = True
        self.gameView.show(
            "\n\x1b[36;1m                                    YOURTURN" + self.options.userNickName + "\x1b[0m\n")
        self.showStats(Mode.INGAME)

        try:
            if self.options.hero.weapon.usage <= 0:
                haveWeapon = False
        except AttributeError:
            haveWeapon = False

        while cooldownBreak:
            cooldownBreak = False
            if haveWeapon:
                self.gameView.show("\n                         ACTIONS: \n1.Attack (" + str(
                    self.options.hero.damage) + " damage)\n2.Use " + self.options.hero.weapon.name + \
                                   " (Number of usage " + str(self.options.hero.weapon.usage) + ", " + str(
                    self.options.hero.weapon.damage) + " - damage" + ")\n3.Use Heal (" + str(
                    numberOfHeal) + ")\n4.Use Mana (" + str(numberOfMana) + ")\n" + \
                                   "5.Use Skill (" + str(self.options.hero.skill.name) + " Damage - " + str(
                    self.options.hero.skill.value) + ")Cooldown " + str(self.heroCooldown) + " turns\n")
            else:
                self.gameView.show("\n                         ACTIONS: \n1.Attack (" + str(
                    self.options.hero.damage) + " damage)\n3.Use Heal (" + str(
                    numberOfHeal) + ")\n4.Use Mana (" + str(numberOfMana) + ")\n" + \
                                   "5.Use Skill (" + str(self.options.hero.skill.name) + " Damage - " + str(
                    self.options.hero.skill.value) + ") Cooldown " + str(self.heroCooldown) + " turns\n")

            action = self.gameView.input()
            if int(action) == 1:
                self.options.enemy.takeDamage(self.options.hero.damage, "\x1b[31;1m  Enermy takes " + str(
                    self.options.hero.damage) + " damage. CAUSE: Basic attack\x1b[0m\n")
            elif int(action) == 2:
                self.options.enemy.takeDamage(self.options.hero.weapon.damage, "\x1b[31;1m  Enermy takes " + str(
                    self.options.hero.weapon.damage) + " damage. CAUSE:  Attack by " + self.options.hero.weapon.name + "\x1b[0m\n")
                self.options.hero.weapon.usage -= 1
            elif int(action) == 3:
                if numberOfHeal > 0:
                    self.options.hero.heal(healthBottle.recoverCount, "\x1b[32;1m Healed " + str(
                        healthBottle.recoverCount) + " hp. CAUSE Heal bottle.\x1b[0m")
                    self.options.hero.removeInventoryItem(healthBottle)
                else:
                    self.gameView.show("NOT ENOGH HEAL BOTTLES.")
                    cooldownBreak = True
            elif int(action) == 4:
                if numberOfMana > 0:
                    self.options.hero.addMana(manaBottle.recoverCount, "\x1b[34;1m Mana increased by " + str(
                        manaBottle.recoverCount) + " hp. CAUSE Mana bottle.\x1b[0m")
                    self.options.hero.removeInventoryItem(manaBottle)
                else:
                    self.gameView.show("NOT ENOGH MANA BOTTLES.")
                    cooldownBreak = True
            elif int(action) == 5:
                if self.heroCooldown == 0:
                    self.gameView.show("CASTING " + str(self.options.hero.skill.name) + "...\n")
                    time.sleep(2)
                    self.options.enemy.takeDamage(self.options.hero.skill.value, "Enemy takes " + str(
                        self.options.hero.skill.value) + " damage. CAUSE used skill " + self.options.hero.skill.name)
                    self.heroCooldown = 3
                else:
                    self.gameView.show("COOLDOWN...")
                    cooldownBreak = True

        if not self.heroCooldown <= 0:
            self.heroCooldown -= 1

        if self.options.hero.health <= 0:
            return "hero"
        elif self.options.enemy.health <=0:
            return "enemy"
        else:
            return None


    def __enemyTurn(self):
        self.showStats(Mode.INGAME)
        # action = random.randint(1,6)

        time.sleep(2)
        action = 1
        heal = None
        mana = None

        for element in self.options.enemy.inventory:
            if not isinstance(element, Weapon):
                if element.price == 400:
                    heal = element
                else:
                    mana = element


        #COMPUTER LOGIC

        if self.options.enemy.health < self.options.enemy.maxHealth / 2 and self.options.hero.health < self.options.hero.maxHealth / 2:
            randomHealOrAttack = random.randint(0, 2)
            if randomHealOrAttack == 0:
                action = 3
            else:
                radomMainDamageAction = random.randint(0, 2)
                if radomMainDamageAction == 0:
                    if self.options.enemy.weapon != None and self.options.enemy.weapon.usage > 0:
                        action = 2
                    else:
                        action = 1
                else:
                    if self.enemyCooldown == 0:
                        action = 5
                        self.enemyCooldown = 3
                    else:
                        action = 1

        elif self.options.enemy.health < self.options.enemy.maxHealth / 2:
            action = 3

        elif self.options.hero.health < self.options.enemy.maxHealth / 2:
            radomMainDamageAction = random.randint(0, 2)
            if radomMainDamageAction == 0:
                if self.options.enemy.weapon != None and self.options.enemy.weapon.usage > 0:
                    action = 2
                else:
                    action = 1
            else:
                if self.enemyCooldown == 0:
                    action = 5
                    self.enemyCooldown = 3

        elif self.options.enemy.mana < self.options.enemy.maxMana / 3 :
            action = 4

        else:
            radomMainDamageAction = random.randint(0, 2)
            if radomMainDamageAction == 0:
                if self.options.enemy.weapon != None and self.options.enemy.weapon.usage > 0:
                    action = 2
                else:
                    action = 1
            else:
                if self.enemyCooldown == 0:
                    action = 5
                    self.enemyCooldown = 3



        if action == 1:
                self.options.hero.takeDamage(self.options.enemy.damage, "\x1b[31;1m  You take " + str(
                    self.options.enemy.damage) + " damage. CAUSE: Basic attack\x1b[0m\n")
        elif action == 2:
            self.options.hero.takeDamage(self.options.enemy.weapon.damage, "\x1b[31;1m  You take " + str(
                self.options.enemy.weapon.damage) + " damage. CAUSE:  Attack by " + self.options.enemy.weapon.name + "\x1b[0m\n")
            self.options.enemy.weapon.usage -= 1
        elif action == 3:
            self.options.enemy.heal(heal.recoverCount, "\x1b[32;1m Enemt Healed " + str(
                heal.recoverCount) + " hp. CAUSE Heal bottle.\x1b[0m")
        elif action == 4:
            self.options.hero.addMana(mana.recoverCount, "\x1b[34;1mEnemy Mana increased by " + str(
                mana.recoverCount) + " hp. CAUSE Mana bottle.\x1b[0m")
        elif action == 5:
                self.gameView.show("Enemy CASTING " + str(self.options.enemy.skill.name) + "...\n")
                time.sleep(2)
                self.options.hero.takeDamage(self.options.enemy.skill.value, "You takes " + str(self.options.enemy.skill.value) + " damage. CAUSE used skill " + self.options.enemy.skill.name)

        time.sleep(3)

        if self.options.hero.health <= 0:
            return "hero"
        elif self.options.enemy.health <= 0:
            return "enemy"
        else:
            return None
#
# def main():
#     Game().startScenario()
#
# main()
#
#









