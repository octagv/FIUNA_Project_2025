import pandas as pd
from .text import *
from utilities.map import createMap, createMark, createHeadMap
from utilities.graph import graphMean, graphMin, graphMax
from db.getData import getStationPoints, getAllData

def help_process(logs):
    if not len(logs):
        print(MAIN_HELP)
    elif len(logs) != 1:
        print("Solo introducir un comando")
    elif logs[0] in COMMANDS_HELP.keys():
        print(COMMANDS_HELP[logs[0]])
    else:
        print("Uso incorrecto")

def graph_process(logs):
    if len(logs) != 1:
        print("Uso incorrecto. Para saber más ejecute: ayuda graficar")
    elif logs[0] == "media":
        graphMean(getAllData())
    elif logs[0] == "maxima":
        graphMax(getAllData())
    elif logs[0] == "minima":
        graphMin(getAllData())
    
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
        createHeadMap(getAllData(), "temperature")
    elif logs[0] == "humedad":
        createHeadMap(getAllData(), "humidity")
    elif logs[0] == "viento":
        createHeadMap(getAllData(), "wind_speed")
    elif logs[0] == "radiacion":
        createHeadMap(getAllData(), "solar_radiation")
    else:
        print("Uso incorrecto. Para saber más ejecute: ayuda mapa")