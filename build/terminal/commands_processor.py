from .text import *
from utilities.map import createMap, createMark
from db.getData import getStationPoints

def help_process(logs):
    if not len(logs):
        print(MAIN_HELP)
    else:
        print(COMMANDS_HELP[logs[0]])

def graph_process(logs):
    if not len(logs):
        print("Uso incorrecto. Para saber más ejecute: ayuda graficar")
    elif len(logs) >= 3 and logs[0] in DATA_NAME and logs[1] in DATA_NAME and logs[2] in DATA_NAME:
        pass
    elif len(logs) >= 2 and logs[0] in DATA_NAME and logs[1] in DATA_NAME:
        pass
    elif len(logs) >= 1 and logs[0] in DATA_NAME:
        pass
    else:
        print("Uso incorrecto. Para saber más ejecute: ayuda graficar")

def map_process(logs):
    if not len(logs):
        print("Uso incorrecto. Para saber más ejecute: ayuda mapa")
    elif logs[0] == "estaciones":
        stations = getStationPoints()
        map = createMap([-25.341975, -57.508483])
        for station in stations:
            createMark(map, station[1::],f"Estacion {station[0]}")
        map.show_in_browser()
    elif logs[0] == "temperatura":
        print("Aun no añadido")
    elif logs[0] == "humedad":
        print("Aun no añadido")
    elif logs[0] == "viento":
        print("Aun no añadido")
    else:
        print("Uso incorrecto. Para saber más ejecute: ayuda mapa")