import random
import time
import sqlite3

from db import (insertData, createdb, deletedb)
def generatePoint():
    return [-25.341975 + random.random(), -57.508483+random.random()]
def generateStations(numOfStations):
    stations = []
    for _ in range(numOfStations):
        stations.append(generatePoint())
    return stations

def generateInfo(numOfStations, numOfLogs):
    stations = generateStations(numOfStations)
    for _ in range(numOfLogs):
        number = random.randint(1,numOfStations)
        insertData.insertEntry((
            time.time(),
            number,
            stations[number-1][0],
            stations[number-1][1],
            36 + 5*random.random(),
            50 + 50*random.random(),
            18 + 10*random.random(),
            50 + 50*random.random()
        ))

if __name__ == "__main__":
    createdb.createDb()
    generateInfo(20, 2)
    print("Se ha creado la informacion")
    conection = sqlite3.connect("db/app_log.db")
    cursor = conection.cursor()
    cursor.execute("SELECT * FROM logs")
    for element in cursor.fetchall():
        print(element[1::])
    conection.close()