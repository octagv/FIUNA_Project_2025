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

MAIN_WELCOME = """
Bienvenido al Sistema Telemetrico de estaciones metereologicas
Digite ayuda para ver los comandos
"""