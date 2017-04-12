import pymysql.cursors

class DataSource:

    # __dataSource = None
    # NO CALL
    # def __init__(self):
    #     self.__host = 'localhost',
    #     self.__user = 'root',
    #     self.__password = 'root',
    #     self.__db = 'pythonconsole',
    #     self.__charset = 'utf8mb4',
    #     self.__cursorclass = pymysql.cursors.DictCursor
    #

    # @staticmethod
    # def getInstance():
    #     if DataSource.__dataSource == None:
    #         DataSource.__dataSource = DataSource()
    #     else:
    #         return DataSource.__dataSource


    def getConnection(self):
        return pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='pythonconsole',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor).cursor()


