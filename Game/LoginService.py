
from UserService import UserService
from UserTO import UserTO
from DAO.UserDAO import UserDAO

class LoginService:

    def __init__(self):
        self.__userService = UserService()
        self.__userDAO = UserDAO()


    # return True if login success othervise returns false
    def login(self, user):
        # TODO ADD DAO
        findedUser = self.__userDAO.find(user.getUsername())

        if findedUser.getPassword() == user.getPassword():
            """upgrade users login state"""
            self.__userDAO.updateLogin()
            user.setLoggedIn()
            return True
        else:
            return False




