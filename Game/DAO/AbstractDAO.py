import pymysql.cursors

from DAO.DataSource import DataSource



""" Class covers mechanism of connecting to db"""
class AbstractDAO:
    def __init__(self, dataSource):
        self.__dataSource = dataSource


    def __executeQuery(self, SQL, params):
        connection = self.__dataSource.getConnection()
        try:
            connection.execute(SQL, params)
            return connection.fetchone()

        finally:
            connection.close()


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