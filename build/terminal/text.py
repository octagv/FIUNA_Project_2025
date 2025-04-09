MAIN_HELP = """
Comandos del Sistema--------------------------------------------------------------------------------
version -> Imprime la version del sistema
creditos -> Imprime informacion acerca de los creadores
future -> Obtendra informacion acerca de funcionalidades futuras
salir -> Sale del sistema

Comandos de Insercion de Datos----------------------------------------------------------------------
-insertar [id estacion] [latitud] [longitud] [temperatura] [humedad] [viento] [radiacion] -> Inserta un log de dato
-insertar_archivo [archivo.csv] -> inserta datos de un archivo csv al sistema

Comandos de Graficacion de Datos--------------------------------------------------------------------
-graficar [eje x] -> Grafica en un grafico 2D 
-graficar [eje x] [eje y] -> Grafica en un grafico 2D 
-graficar [eje x] [eje y] [eje z]-> Grafica en un grafico 3D
-mapa [datos] -> Genera un mapa de calor del dato especifico

Comandos Matematicos--------------------------------------------------------------------------------
-maximo
-minimo
-media

Comandos de Base de Datos---------------------------------------------------------------------------
-crear_tabla
-eliminar_tabla
-ver_datos

Comandos de Prueba----------------------------------------------------------------------------------
-generar [nro de estaciones] [nro de logs] -> genera un numero definido de logs de una cantidad de estaciones dadas
"""
COMMANDS_HELP = {
    "ayuda" : "Comando que da informacion acerca de otras funciones",
    "version" : "Devuelve la version del sistema",
    "creditos" : "Informacion acerca de los creadores",
    "graficar" : "Aun no añadido",
    "mapa" : "Aun no añadido",
    "insertar" : "Aun no añadido",
    "crear_tabla" : "Aun no añadido",
    "eliminar_tabla" : "Aun no añadido",
    "ver_datos" : "Aun no añadido",
    "exportar" : "Aun no añadido"
}


MAIN_WELCOME = """
Bienvenido al Sistema Telemetrico de estaciones metereologicas
Digite ayuda para ver los comandos
"""

DATA_NAME = ["temperatura", "humedad", "viento"]

VERSION_TEXT = "Version beta 0.1"
CREDIT_TEXT = "Programa creado por Octavio Gauto y Tobias Recasens. Como parte del proyecto desafio de la materia fundamentos de programación"