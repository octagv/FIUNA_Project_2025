import random
import time
import sqlite3

from db import (insertData, createdb, deletedb)

#stations = [(-27.22,-55.83),(-27.2,-55.78),(-26.87,-58.32),(-26.83,-55.32),(-26.67,-57.13),(-26.17,-56.35),(-25.75,-56.43),(-25.62,-57.13),(-25.5,-56.4),(-25.45,-54.83)]
temps = [20,30,35,27,12,8,17]
def generatePoint():
    return [-25.341975 + random.random(), -57.508483+random.random()]
def generateStations(numOfStations):
    stations = []
    for _ in range(numOfStations):
        stations.append(generatePoint())
    return stations

def generateInfo(numOfStations, numOfLogs):
    #stations = generateStations(numOfStations)
    stations = [(-27.22,-55.83),(-27.2,-55.78),(-26.87,-58.32),(-26.83,-55.32),(-26.67,-57.13),(-26.17,-56.35),(-25.75,-56.43),(-25.62,-57.13),(-25.5,-56.4),(-25.45,-54.83)]
    base_time = 1704078000
    datatable = []
    for j in range(numOfLogs):
        log_time = base_time + (j * 86400)
        log_temp = random.choice(temps)
        for i in range(len(stations)):
            datatable.append((
                log_time,
                i,
                stations[i][0],
                stations[i][1],
                log_temp + random.randint(0,10), #temperatura
                random.randint(27,100), #humedad
                random.randint(6,32), #viento
                random.randint(32,100) #radiacion
            ))
    insertData.insertData(datatable)
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