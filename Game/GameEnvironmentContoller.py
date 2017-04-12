
# import LoginService
# from Game import View

from View import View
from UserService import UserService
from LoginService import LoginService
from UserTO import UserTO
from LoginException import LoginException

class GameEnvironmentContoller:

    def __init__(self):
        # self.__game = Game()
        # self.__gameOptions = GameOptions()
        self.__loginService = LoginService()
        self.__user = None
        self.__view = View()



    def start(self):
        # show login and harvest data (username, password)
        valid = False
        self.__view.show("Welcome to Notewel")
        while not valid:
            try:
                action = int(self.__view.input("1. Sign in \n2. Sign Up\n"))

                if action == 1:

                    username = self.__view.input("Enter username")
                    password = self.__view.input("Enter password")

                    # login action
                    if UserService.validateUsername(username) and UserService.validatePassword(password):
                        user = UserTO(username, password)
                        if self.__loginService.login(user):
                            self.__user = user
                            print(str(self.__user))
                            # Set up game options and start game
                        else:
                            raise LoginException("Check your password.")

                        valid = True
                    else:
                        raise AttributeError("Username and passwrod must be at least 6 character\n")

            except ValueError:
                self.__view.err("Invalid param\n")
            except AttributeError as e:
                self.__view.err(e)










def main():
    GameEnvironmentContoller().start()

main()