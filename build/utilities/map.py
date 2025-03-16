import folium
import math
import random
"""Funcion que genera la base del mapa"""
def createMap(initPoint):
    return folium.Map(initPoint, zoom_start=10,max_zoom=10)
"""Funcion que introduce un marcador al mapa"""
def createMark(map, point, point_name):
    folium.Marker(point,popup=point_name).add_to(map)

def createHeadMap():
    pass

if __name__ == "__main__":
    map = createMap([-25.341975 + random.random(), -57.508483+random.random()])
    for i in range(1,21):
        createMark(map,[-25.341975 + random.random(), -57.508483+random.random()],f"Estacion {i}")
    map.show_in_browser()