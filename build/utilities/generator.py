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
    base_time = int(time.time()) 
    for j in range(numOfLogs):
        log_time = base_time - (j * 1800)
        for i in range(numOfStations):
            insertData.insertEntry((
                log_time,
                i,
                stations[i][0],
                stations[i][1],
                random.randint(20,41), #temperatura
                random.randint(0,100), #humedad
                random.randint(6,32), #viento
                random.randint(0,100) #radiacion
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