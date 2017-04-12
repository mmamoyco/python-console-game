import pymysql.cursors

# from DAO.DataSource import DataSource
from UserService import UserService
from DAO.AbstractDAO import AbstractDAO
from DAO.DataSource import DataSource


class UserDAO(AbstractDAO):

    def __init__(self):
        AbstractDAO.__init__(self, DataSource())


    def find(self, username):
        """Find user by username"""
        SQL = "Select * from user where username = %s "
        params = [].append(username)

        return UserService.parse(self.__executeQuery(SQL, tuple(params)))


    # def updateLogin(self):


#
# import pymysql.cursors
#
# # Connect to the database
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='root',
#                              db='pythonconsole',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)
#
# try:
#
#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT * FROM `user`"
#         cursor.execute(sql)
#         result = cursor.fetchone()
#         print(result)
# finally:
#     connection.close()