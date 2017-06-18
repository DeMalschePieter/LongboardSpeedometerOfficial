import mysql.connector as connector

class DbClass:
    def __init__(self):


        self.__dsn = {
            "host": "localhost",
            "user": "pierre",
            "passwd": "geheim",
            "db": "TLSDatabase"
        }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def getDeelSessies(self):
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()
        # Query zonder parameters
        sqlQuery = "SELECT * FROM tbl_deelsessie"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getSessies(self):
        # Query zonder parameters
        sqlQuery = "SELECT * FROM tbl_sessies"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getLaatsteRegelSessies(self):
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()
        # Query zonder parameters
        sqlQuery = "SELECT * FROM tbl_sessies ORDER BY id_sessie DESC LIMIT 1"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def get4LaatsteRegelsSessies(self):
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()
        # Query zonder parameters
        sqlQuery = "SELECT * FROM tbl_sessies ORDER BY id_sessie DESC LIMIT 4"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getLaatsteRegelDeelSessies(self):
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()
        # Query zonder parameters
        sqlQuery = "SELECT * FROM tbl_deelsessie ORDER BY id_sessie DESC LIMIT 1"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getLaatste5RegelsDeelsessies(self, id):
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()
        # Query zonder parameters
        sqlQuery = "SELECT * FROM tbl_deelsessie WHERE id_sessie = '"+str(id)+"' ORDER BY id_sessie DESC LIMIT 6 "

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getBepaaldeDeelsessies(self, id):
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()
        # Query zonder parameters
        sqlQuery = "SELECT * FROM tbl_deelsessie WHERE id_sessie = '"+str(id)+"' "

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result



    def getDataFromDatabaseMetVoorwaarde(self, voorwaarde):
        # Query met parameters
        sqlQuery = "SELECT * FROM tablename WHERE columnname = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def setDeelsessie(self, time, distance, speed, id_sessie):
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()
        # Query met parameters
        sqlQuery = "INSERT INTO tbl_deelsessie(time,distance,speed,id_sessie)" \
                   "VALUES  ('"+time+"','" + str(distance) + "','" + str(speed) + "','" + str(id_sessie) + "')"
        # Combineren van de query en parameter
        # sqlCommand = sqlQuery.format(param1=value1)

        self.__cursor.execute(sqlQuery)
        self.__connection.commit()
        self.__cursor.close()

    def setSessie(self,starttijd,einddtijd,distance,max_speed,averagespeed,id_rider,inGebruik):
        # Query met parameters
        sqlQuery = "INSERT INTO tbl_sessies(starttijd,eindtijd,distance,max_speed,average_speed,id_rider,inGebruik)" \
                   "VALUES ('"+starttijd+"','" + einddtijd + "','" + str(distance) + "','" + str(max_speed) + "','" + str(averagespeed) + "','" + str(id_rider) + "','" + str(inGebruik) + "')"
        # Combineren van de query en parameter
        # sqlCommand = sqlQuery.format(param1=value1)

        self.__cursor.execute(sqlQuery)
        self.__connection.commit()
        self.__cursor.close()

    def UpdateSession(self,id_sessie,einddtijd,distance,max_speed,averagespeed,id_rider,inGebruik):
        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()
        # Query met parameters
        sqlQuery = "UPDATE tbl_sessies SET eindtijd = '"+str(einddtijd)+"', distance = '"+str(distance)+"', max_speed = '"+str(max_speed)+"', average_speed = '"+str(averagespeed)+"', id_rider = '"+str(id_rider)+"', inGebruik = '"+str(inGebruik)+"' WHERE id_sessie = '"+str(id_sessie)+"'"
        # Combineren van de query en parameter
        # sqlCommand = sqlQuery.format(param1=value1)

        self.__cursor.execute(sqlQuery)
        self.__connection.commit()
        self.__cursor.close()