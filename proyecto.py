import os
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium, folium.plugins
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
    table = pd.read_csv(csv,header=1, sep=";")
    conection = sqlite3.connect("app_log.db")
    cursor = conection.cursor()
    for line in table.itertuples(index=False):
        cursor.execute("INSERT INTO logs (time, id_station, latitud, longitud, temperature, humidity, wind_speed, solar_radiation) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       line[1::])
    conection.commit()
    conection.close()
def getAllData():
    con = sqlite3.connect("app_log.db")
    df = pd.read_sql_query("SELECT * FROM logs", con)
    con.close()
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df
def getStationPoints():
    conection = sqlite3.connect("app_log.db")
    cursor = conection.cursor()
    cursor.execute("SELECT DISTINCT id_station, latitud, longitud FROM logs")
    data = cursor.fetchall()
    conection.close()
    return data
def exportData():
    con = sqlite3.connect("app_log.db")
    df = pd.read_sql_query("SELECT * FROM logs", con)
    con.close()
    df.to_csv("datos_exportados.csv", index=False , sep=";")

#FUNCIONES DE MAPA
def createHeadMapWind(data):
    data['time'] = pd.to_datetime(data['time']).dt.strftime(r'%Y-%m-%d')
    time_index = sorted(data['time'].unique())
    heat_data = []
    for t in time_index:
        subset = data[data['time'] == t]
        frame_points = [[row['latitud'], row['longitud'], row["wind_speed"]  / 80] for _, row in subset.iterrows()]
         # Agregar puntos fuera del mapa solo para fijar escala
        frame_points.append([0, 0, 0])     # punto ficticio para el mínimo
        frame_points.append([0, 0, 1])     # punto ficticio para el máximo
        heat_data.append(frame_points)

    # Crear mapa base centrado
    m = folium.Map(location=[data['latitud'].mean(), data['longitud'].mean()], zoom_start=10, max_zoom=10, min_zoom=5)

    #Agregar marcadores
    for station in getStationPoints():
        folium.Marker(station[1::],popup=f"Estacion {station[0]}").add_to(m)

    # Agregar mapa de calor con tiempo
    folium.plugins.HeatMapWithTime(
        heat_data,
        index=time_index,
        auto_play=False,
        radius=200,
        max_opacity=0.8,
        use_local_extrema=True,
        gradient={0.0: '#b3ecff', 0.3: '#3399ff', 0.6: '#3366cc', 1.0: '#6600cc'}
    ).add_to(m)

    # Guardar mapa
    m.save('./results/heatmap_de_velocidad_viento.html')

def createHeadMapRad(data):
    data['time'] = pd.to_datetime(data['time']).dt.strftime(r'%Y-%m-%d')
    time_index = sorted(data['time'].unique())
    heat_data = []
    for t in time_index:
        subset = data[data['time'] == t]
        frame_points = [[row['latitud'], row['longitud'], row["solar_radiation"]  / 2000] for _, row in subset.iterrows()]
        frame_points.append([0, 0, 0])     # punto ficticio para el mínimo
        frame_points.append([0, 0, 1])     # punto ficticio para el máximo
        heat_data.append(frame_points)

    # Crear mapa base centrado
    m = folium.Map(location=[data['latitud'].mean(), data['longitud'].mean()], zoom_start=10, max_zoom=10, min_zoom=5)

    #Agregar marcadores
    for station in getStationPoints():
        folium.Marker(station[1::],popup=f"Estacion {station[0]}").add_to(m)

    # Agregar mapa de calor con tiempo
    folium.plugins.HeatMapWithTime(
        heat_data,
        index=time_index,
        auto_play=False,
        radius=200,
        max_opacity=0.8,
        use_local_extrema=True,
        gradient={0.0: 'blue', 0.2: 'cyan', 0.5: 'yellow', 0.8: 'orange', 1.0: 'red'}
    ).add_to(m)

    # Guardar o mostrar
    m.save('./results/heatmap_de_radiacion_solar.html')

#FUNCIONES DE GRAFICAS
def createWindGraph(data):
    # Crear una copia para no modificar el DataFrame original
    df_temp = data[['time', 'wind_speed']].copy()
    
    # Asegurarse de que 'fecha' sea tipo datetime
    df_temp['fecha'] = pd.to_datetime(df_temp['time'])

    # Extraer el número del mes
    df_temp['mes'] = df_temp['fecha'].dt.month

    # Agrupar por mes y calcular estadísticas
    resumen = df_temp.groupby('mes')['wind_speed'].agg(['max', 'mean', 'min']).sort_index()

    # Crear el gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(resumen.index, resumen['max'], color='red', marker='o', label='Máxima')
    plt.plot(resumen.index, resumen['mean'], color='gold', marker='o', label='Media')
    plt.plot(resumen.index, resumen['min'], color='blue', marker='o', label='Mínima')

    # Etiquetas y estilo
    plt.title('Velocidades mensuales')
    plt.xlabel('Mes')
    plt.ylabel('Viento (km/h)')
    plt.xticks(range(1, 13), 
               ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
                'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("./results/VientoMensual.png", dpi=300)
def createRadGraph(data):
    # Crear una copia para no modificar el DataFrame original
    df_temp = data[['time', 'solar_radiation']].copy()
    
    # Asegurarse de que 'fecha' sea tipo datetime
    df_temp['fecha'] = pd.to_datetime(df_temp['time'])

    # Extraer el número del mes
    df_temp['mes'] = df_temp['fecha'].dt.month

    # Agrupar por mes y calcular estadísticas
    resumen = df_temp.groupby('mes')['solar_radiation'].agg(['max', 'mean', 'min']).sort_index()

    # Crear el gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(resumen.index, resumen['max'], color='red', marker='o', label='Máxima')
    plt.plot(resumen.index, resumen['mean'], color='gold', marker='o', label='Media')
    plt.plot(resumen.index, resumen['min'], color='blue', marker='o', label='Mínima')

    # Etiquetas y estilo
    plt.title('Radiacion mensual')
    plt.xlabel('Mes')
    plt.ylabel('Radiacion Solar (%)')
    plt.xticks(range(1, 13), 
               ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
                'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("./results/RadSolarMensual.png", dpi=300)


def graphStats(data):

    # Agrupar por estación y calcular la media
    medias = data.groupby('id_station')['temperature'].mean().sort_index()

    # Configurar datos para el gráfico
    estaciones = medias.index.astype(str)
    x = np.arange(len(estaciones))

    # Generar colores únicos por barra usando una colormap
    cmap = plt.colormaps['tab10'] 
    colores = [cmap(i % cmap.N) for i in range(len(estaciones))]

    # Crear gráfico de barras
    plt.figure(figsize=(10, 6))
    barras = plt.bar(x, medias.values, color=colores, width=0.6)

    # Ajuste del eje Y dinámico
    y_min = medias.min()
    y_max = medias.max()
    margen = (y_max - y_min) * 0.1 if y_max != y_min else 1  # evitar margen cero

    plt.ylim(y_min - margen, y_max + margen)

    # Etiquetas
    plt.xlabel('Estación')
    plt.ylabel('Temperatura media (°C)')
    plt.title('Temperatura media por estación')
    plt.xticks(x, estaciones)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Agregar etiquetas numéricas sobre cada barra
    for i, valor in enumerate(medias.values):
        plt.text(x[i], valor + margen * 0.05, f'{valor:.2f}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig('./results/temperatura_estaciones.png', dpi=300)

    #Humedades
     # Agrupar por estación y calcular la media
    medias = data.groupby('id_station')['humidity'].mean().sort_index()

    # Configurar datos para el gráfico
    estaciones = medias.index.astype(str)
    x = np.arange(len(estaciones))

    # Crear gráfico de barras
    plt.figure(figsize=(10, 6))
    barras = plt.bar(x, medias.values, color=colores, width=0.6)

    # Ajuste del eje Y dinámico
    y_min = medias.min()
    y_max = medias.max()
    margen = (y_max - y_min) * 0.1 if y_max != y_min else 1  # evitar margen cero

    plt.ylim(y_min - margen, y_max + margen)

    # Etiquetas
    plt.xlabel('Estación')
    plt.ylabel('Humedad media (%)')
    plt.title('Humedad media por estación')
    plt.xticks(x, estaciones)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Agregar etiquetas numéricas sobre cada barra
    for i, valor in enumerate(medias.values):
        plt.text(x[i], valor + margen * 0.05, f'{valor:.2f}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig('./results/humedad_estaciones.png', dpi=300)

    # Agrupar por estación y calcular la media
    medias = data.groupby('id_station')['wind_speed'].mean().sort_index()

    # Configurar datos para el gráfico
    estaciones = medias.index.astype(str)
    x = np.arange(len(estaciones))

    # Crear gráfico de barras
    plt.figure(figsize=(10, 6))
    barras = plt.bar(x, medias.values, color=colores, width=0.6)

    # Ajuste del eje Y dinámico
    y_min = medias.min()
    y_max = medias.max()
    margen = (y_max - y_min) * 0.1 if y_max != y_min else 1  # evitar margen cero

    plt.ylim(y_min - margen, y_max + margen)

    # Etiquetas
    plt.xlabel('Estación')
    plt.ylabel('Viento media (km/h)')
    plt.title('Viento media por estación')
    plt.xticks(x, estaciones)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Agregar etiquetas numéricas sobre cada barra
    for i, valor in enumerate(medias.values):
        plt.text(x[i], valor + margen * 0.05, f'{valor:.2f}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig('./results/viento_estaciones.png', dpi=300)


    # Parámetros
    rho = 1.225  # Densidad del aire en kg/m^3
    area = 1.0   # Área del rotor en m^2 (ajusta este valor según tu turbina)

    # Calcular potencia eólica
    potencia_eolica = 0.6 * rho * area * (medias/3.6)**3
    
    # Graficar
    plt.figure(figsize=(10, 6))
    potencia_eolica.plot(kind='bar', color=colores)
    plt.title('Potencia eólica posible por estación')
    plt.xlabel('ID de estación')
    plt.ylabel('Potencia generada (W/m2)')

    # Ajuste del eje Y dinámico
    y_min = potencia_eolica.min()
    y_max = potencia_eolica.max()
    margen = (y_max - y_min) * 0.1 if y_max != y_min else 1  # evitar margen cero

    plt.ylim(y_min - margen, y_max + margen)

    plt.grid(True)
    # Agregar etiquetas numéricas sobre cada barra
    for i, valor in enumerate(potencia_eolica.values):
        plt.text(x[i], valor + margen * 0.05, f'{valor:.2f}', ha='center', va='bottom', fontsize=9)
    plt.tight_layout()
    plt.savefig('./results/PotenciaEolica_estaciones.png')

    # Agrupar por estación y calcular la media
    medias = data.groupby('id_station')['solar_radiation'].mean().sort_index()

    # Configurar datos para el gráfico
    estaciones = medias.index.astype(str)
    x = np.arange(len(estaciones))

    # Crear gráfico de barras
    plt.figure(figsize=(10, 6))
    barras = plt.bar(x, medias.values, color=colores, width=0.6)

    # Ajuste del eje Y dinámico
    y_min = medias.min()
    y_max = medias.max()
    margen = (y_max - y_min) * 0.1 if y_max != y_min else 1  # evitar margen cero

    plt.ylim(y_min - margen, y_max + margen)

    # Etiquetas
    plt.xlabel('Estación')
    plt.ylabel('Radiación media (W/m2)')
    plt.title('radiación solar media por estación')
    plt.xticks(x, estaciones)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Agregar etiquetas numéricas sobre cada barra
    for i, valor in enumerate(medias.values):
        plt.text(x[i], valor + margen * 0.05, f'{valor:.2f}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig('./results/radiacion_estaciones.png', dpi=300)

    eficiencia = 0.18  # Eficiencia Panel Solar
    area = 1  # en metros cuadrados

    # Calcular potencia generada
    potencia_solar = medias * eficiencia * area

    cmap = plt.colormaps['tab10']  # Puedes cambiar a 'tab20', 'Set3', etc.
    colores = [cmap(i % cmap.N) for i in range(len(estaciones))]
    # Graficar
    plt.figure(figsize=(10, 6))
    potencia_solar.plot(kind='bar', color=colores)

    # Ajuste del eje Y dinámico
    y_min = potencia_solar.min()
    y_max = potencia_solar.max()
    margen = (y_max - y_min) * 0.1 if y_max != y_min else 1  # evitar margen cero

    plt.ylim(y_min - margen, y_max + margen)

    plt.title('Potencia Solar Posible por estación')
    plt.xlabel('ID de estación')
    plt.ylabel('Potencia generada (W/m²)')

    plt.grid(True)
     # Agregar etiquetas numéricas sobre cada barra
    for i, valor in enumerate(potencia_solar.values):
        plt.text(x[i], valor + margen * 0.05, f'{valor:.2f}', ha='center', va='bottom', fontsize=9)
    plt.tight_layout()
    plt.savefig("./results/potencia_solar.png", dpi=300)


#PROGRAMA PRINCIPAL
createDb()
print("Bienvenido al Sistema")
while(True):
    print("--------------------------------")
    print("Elija una opcion:")
    print("""
    1) Resetear Base de Datos
    2) Ingresar Dato Manualmente
    3) Ingresar Archivo CSV
    4) Generar Informe
    5) Exportar Datos a CSV
    6) Salir
    """)
    opt = input("Ingrese una opcion:  ")
    print("")

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
            print("Archivos Insertados Correctamente")
        except Exception as e:
            print(e)
            print("Error: Archivo no existe")
    elif (opt == "4"):
        data = getAllData()
        if not len(data):
            print("No hay datos para generar los resultados")
        else:
            if not os.path.exists("results"):
                os.makedirs("results")
            createHeadMapWind(data)
            createHeadMapRad(data)
            createWindGraph(data)
            createRadGraph(data)
            graphStats(data)
            print("Graficos y Mapas Generados")
    elif (opt == "5"):
        if not len(getAllData()):
            print("No hay datos para exportar")
        else:
            exportData()
            print("Datos exportados")
    elif(opt == "6"):
        print("Hasta Luego")
        break
    else:
        print("Comando Desconocido")