import sqlite3
import pandas as pd
import folium
#FUNCIONES DE BASE DE DATOS
def createDb():
    conection = sqlite3.connect("app_log.db")
    cursor = conection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS logs
                (id integer primary key autoincrement,
                time integer,
                id_station integer, 
                latitud real, 
                longitud real, 
                temperature real,
                humidity real,
                wind_speed real,
                solar_radiation real
                )''')

    conection.commit()
    conection.close()
def deleteDb():
    conection = sqlite3.connect("app_log.db")
    cursor = conection.cursor()

    cursor.execute('''DROP TABLE IF EXISTS logs''')

    conection.commit()
    conection.close()
def insertEntry(data):
    conection = sqlite3.connect("app_log.db")
    cursor = conection.cursor()
    cursor.execute("INSERT INTO logs (time, id_station, latitud, longitud, temperature, humidity, wind_speed, solar_radiation) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
    data)
    conection.commit()
    conection.close() 
def insertDatafromCsv(csv):
    table = pd.read_csv(csv,header=None, sep=";")
    conection = sqlite3.connect("app_log.db")
    cursor = conection.cursor()
    for line in table.itertuples(index=False):
        cursor.execute("INSERT INTO logs (time, id_station, latitud, longitud, temperature, humidity, wind_speed, solar_radiation) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       line)
    conection.commit()
    conection.close()
def getAllData():
    con = sqlite3.connect("app_log.db")
    df = pd.read_sql_query("SELECT * FROM logs", con)
    con.close()
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df
def exportData():
    con = sqlite3.connect("db/app_log.db")
    df = pd.read_sql_query("SELECT * FROM logs", con)
    con.close()
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.to_csv("logs_export.csv", index=False)

#FUNCIONES DE MAPA
def createHeadMapTemp(data):
    data['time'] = pd.to_datetime(data['time']).dt.strftime(r'%Y-%m-%d')
    time_index = sorted(data['time'].unique())
    heat_data = []
    for t in time_index:
        subset = data[data['time'] == t]
        frame_points = [[row['latitud'], row['longitud'], row['temperature']] for _, row in subset.iterrows()]
        heat_data.append(frame_points)

    # Crear mapa base centrado
    m = folium.Map(location=[data['latitud'].mean(), data['longitud'].mean()], zoom_start=10, max_zoom=10)

    # Agregar mapa de calor con tiempo
    folium.plugins.HeatMapWithTime(
        heat_data,
        index=time_index,
        auto_play=True,
        radius=60,
        max_opacity=0.8,
        use_local_extrema=False,
        gradient={0.0: 'blue', 0.2: 'cyan', 0.5: 'yellow', 0.8: 'orange', 1.0: 'red'}
    ).add_to(m)

    # Guardar o mostrar
    m.save('resultados/heatmap_de_temperatura.html')
def createHeadMapHum(data):
    data['time'] = pd.to_datetime(data['time']).dt.strftime(r'%Y-%m-%d')
    time_index = sorted(data['time'].unique())
    heat_data = []
    for t in time_index:
        subset = data[data['time'] == t]
        frame_points = [[row['latitud'], row['longitud'], row['temperature']] for _, row in subset.iterrows()]
        heat_data.append(frame_points)

    # Crear mapa base centrado
    m = folium.Map(location=[data['latitud'].mean(), data['longitud'].mean()], zoom_start=10, max_zoom=10)

    # Agregar mapa de calor con tiempo
    folium.plugins.HeatMapWithTime(
        heat_data,
        index=time_index,
        auto_play=True,
        radius=60,
        max_opacity=0.8,
        use_local_extrema=False,
        gradient={0.0: 'blue', 0.2: 'cyan', 0.5: 'yellow', 0.8: 'orange', 1.0: 'red'}
    ).add_to(m)

    # Guardar o mostrar
    m.save('resultados/heatmap_de_humedad.html')
def createHeadMapWind(data):
    data['time'] = pd.to_datetime(data['time']).dt.strftime(r'%Y-%m-%d')
    time_index = sorted(data['time'].unique())
    heat_data = []
    for t in time_index:
        subset = data[data['time'] == t]
        frame_points = [[row['latitud'], row['longitud'], row['temperature']] for _, row in subset.iterrows()]
        heat_data.append(frame_points)

    # Crear mapa base centrado
    m = folium.Map(location=[data['latitud'].mean(), data['longitud'].mean()], zoom_start=10, max_zoom=10)

    # Agregar mapa de calor con tiempo
    folium.plugins.HeatMapWithTime(
        heat_data,
        index=time_index,
        auto_play=True,
        radius=60,
        max_opacity=0.8,
        use_local_extrema=False,
        gradient={0.0: 'blue', 0.2: 'cyan', 0.5: 'yellow', 0.8: 'orange', 1.0: 'red'}
    ).add_to(m)

    # Guardar o mostrar
    m.save('resultados/heatmap_de_velocidad_viento.html')
def createHeadMapRad(data):
    data['time'] = pd.to_datetime(data['time']).dt.strftime(r'%Y-%m-%d')
    time_index = sorted(data['time'].unique())
    heat_data = []
    for t in time_index:
        subset = data[data['time'] == t]
        frame_points = [[row['latitud'], row['longitud'], row['temperature']] for _, row in subset.iterrows()]
        heat_data.append(frame_points)

    # Crear mapa base centrado
    m = folium.Map(location=[data['latitud'].mean(), data['longitud'].mean()], zoom_start=10, max_zoom=10)

    # Agregar mapa de calor con tiempo
    folium.plugins.HeatMapWithTime(
        heat_data,
        index=time_index,
        auto_play=True,
        radius=60,
        max_opacity=0.8,
        use_local_extrema=False,
        gradient={0.0: 'blue', 0.2: 'cyan', 0.5: 'yellow', 0.8: 'orange', 1.0: 'red'}
    ).add_to(m)

    # Guardar o mostrar
    m.save('resultados/heatmap_de_radiacion_solar.html')

#FUNCIONES DE GRAFICAS
def createTempGraph(data):
    pass
def createHumGraph(data):
    pass
def createWindGraph(data):
    pass
def createHumGraph(data):
    pass
#PROGRAMA PRINCIPAL
createDb()
print("Bienvenido al Sistema")
while(True):
    print("Elija una opcion")
    print("""
    1) Resetear Base de Datos
    2) Ingresar Dato Manualmente
    3) Ingresar Archivo CSV
    4) Generar Informe
    5) Exportar Datos a CSV
    6) Salir
    """)
    opt = input("Ingrese una opcion:  ")

    if (opt == "1"):
        deleteDb()
        createDb()
        print("Datos Reiniciados")
    elif (opt == "2"):
        print("Ingrese la informacion solicitada")
        try:
            time = int(input("Tiempo en Unix: "))
            id = int(input("Id de la Estacion: "))
            lat = float(input("Latitud de la Estacion: "))
            lon = float(input("Longitud de la Estacion: "))
            temp = float(input("Temperatura en Celsius: "))
            hum = float(input("Porcentaje de Humedad: "))
            wind = float(input("Velocidad del Viento: "))
            rad = float(input("Porcentaje de Radiacon Solar: "))
            insertEntry((time,id,lat,lon,temp,hum,wind,rad))
        except:
            print("Error al introducir datos")
    elif (opt == "3"):
        filename = input("Ingrese el nombre del archivo:  ")
        try:
            insertDatafromCsv(filename)
        except:
            print("Error: Archivo no existe")
    elif (opt == "4"):
        data = getAllData()
        createHeadMapTemp(data)
        createHeadMapHum(data)
        createHeadMapWind(data)
        createHeadMapRad(data)
        print("Graficos y Mapas Generados")
    elif (opt == "5"):
        exportData()
        print("Datos exportados")
    elif(opt == "6"):
        print("Hasta Luego")
        break
    else:
        print("Comando Desconocido")