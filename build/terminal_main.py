import re
from terminal import text
from utilities.generator import generateInfo
from utilities.map import createMap, createMark

from db.getData import getStationPoints
from db.createdb import createDb
from db.deletedb import deleteDb
from db.insertData import *
def showHelp(command):
    if len(command) == 1:
        print(text.MAIN_HELP)
print(text.MAIN_WELCOME)
while True:
    print(">>", end="")
    command= input()
    command = command.strip()
    command = command.lower()
    command = re.split(" +", command)
    print(command)

    if command[0] == "salir":
        break
    elif command[0] == "generar":
        generateInfo(int(command[1]), int(command[2]))
        print("Informacion Generada")
    elif command[0] == "mapa":
        if command[1] == "estaciones":
            stations = getStationPoints()
            map = createMap([-25.341975, -57.508483])
            for station in stations:
                createMark(map, station[1::],f"Estacion {station[0]}")
            map.show_in_browser()
    elif command[0] == "ayuda":
        showHelp(command)
    elif command[0] == "eliminar_tabla":
        deleteDb()
        print("Tabla Eliminada")
    elif command[0] == "crear_tabla":
        createDb()
        print("Tabla Creada")
    else:
        print("Comando desconocido\n Digite ayuda para ver los comandos")
        