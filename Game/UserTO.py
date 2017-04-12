class UserTO:

    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__loggedIn = False
        # self.__metaData = metaData()


    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password

    def setUsername(self, username):
        self.__username = username

    def isLoggedIn(self):
        return self.__loggedIn

    def setLoggedIn(self):
        self.__loggedIn = not self.__loggedIn

    def __str__(self):
        return "User: " + self.__username