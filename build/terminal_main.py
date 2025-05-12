import re
from terminal import text
from terminal import commands_processor
from utilities.generator import generateInfo
from utilities.map import createMap, createMark

from db.getData import exportData
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
    elif command[0] == "version":
        print(text.VERSION_TEXT)
    elif command[0] == "creditos":
        print(text.CREDIT_TEXT)
    elif command[0] == "generar":
        generateInfo(int(command[1]), int(command[2]))
        print("Informacion Generada")
    elif command[0] == "mapa":
        commands_processor.map_process(command[1::])
    elif command[0] == "media":
        print("Aun no añadido")
    elif command[0] == "maxima":
        print("Aun no añadido")
    elif command[0] == "minima":
        print("Aun no añadido")
    elif command[0] == "ayuda":
        commands_processor.help_process(command[1::])
    elif command[0] == "eliminar_tabla":
        deleteDb()
        print("Tabla Eliminada")
    elif command[0] == "crear_tabla":
        createDb()
        print("Tabla Creada")
    elif command[0] == "graficar":
        commands_processor.graph_process(command[1::])
    elif command[0] == "exportar":
        exportData()
        print("Aun no añadido")
    else:
        print("Comando desconocido\n Digite ayuda para ver los comandos")
        