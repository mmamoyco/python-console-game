from UserTO import UserTO
class UserService:


    @staticmethod
    def validateUsername(username):
        # check for unic username
        return True if len(username) >= 6 else False


    @staticmethod
    def validatePassword(password):
        return True if len(password) >= 6 else False


    @staticmethod
    def parse(map):
        """Parse string repr of onject into real object"""
        if map == None:
            raise AttributeError("No such user")
        return UserTO(map['username'], map['password'])


    # def save