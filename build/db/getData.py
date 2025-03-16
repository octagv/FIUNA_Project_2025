import sqlite3

def getStationPoints():
    conection = sqlite3.connect("db/app_log.db")
    cursor = conection.cursor()
    cursor.execute("SELECT DISTINCT id_station, latitud, longitud FROM logs")
    data = cursor.fetchall()
    conection.close()
    return data
def getAllData():
    conection = sqlite3.connect("db/app_log.db")
    cursor = conection.cursor()
    cursor.execute("SELECT * FROM logs")
    data = cursor.fetchall()
    conection.close()
    return data
