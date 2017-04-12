class LoginException(AttributeError):

    def __init__(self, message):
        self.message = message
        super(LoginException, self).__init__(message)