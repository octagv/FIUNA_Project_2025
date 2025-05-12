import folium
import math
import folium.plugins
import pandas as pd
import random
"""Funcion que genera la base del mapa"""
def createMap(initPoint):
    return folium.Map(initPoint, zoom_start=10,max_zoom=10)
"""Funcion que introduce un marcador al mapa"""
def createMark(map, point, point_name):
    folium.Marker(point,popup=point_name).add_to(map)

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
        radius=80,
        max_opacity=0.8,
        use_local_extrema=False,
        gradient={0.0: 'blue', 0.2: 'cyan', 0.5: 'yellow', 0.8: 'orange', 1.0: 'red'}
    ).add_to(m)

    # Guardar o mostrar
    m.save('heatmap_con_tiempo.html')

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
    m.save('heatmap_con_tiempo.html')

def createHeadMap(data, typedata):
    data['time'] = pd.to_datetime(data['time']).dt.strftime(r'%Y-%m-%d')
    time_index = sorted(data['time'].unique())
    heat_data = []
    for t in time_index:
        subset = data[data['time'] == t]
        frame_points = [[row['latitud'], row['longitud'], row[typedata]  / 50] for _, row in subset.iterrows()]
        heat_data.append(frame_points)

    # Crear mapa base centrado
    m = folium.Map(location=[data['latitud'].mean(), data['longitud'].mean()], zoom_start=10, max_zoom=10)

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
    m.save('heatmap_con_tiempo.html')

if __name__ == "__main__":
    map = createMap([-25.341975 + random.random(), -57.508483+random.random()])
    for i in range(1,21):
        createMark(map,[-25.341975 + random.random(), -57.508483+random.random()],f"Estacion {i}")
    map.show_in_browser()