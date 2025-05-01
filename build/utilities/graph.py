import matplotlib.pyplot as mp
import numpy as np
import pandas as pd
def graph2D(x_values,y_values, x_title, y_title, graph_title):
    mp.figure(figsize=(8, 5))
    mp.plot(x_values, y_values, color="b")

    # Añadir etiquetas y título
    mp.xlabel(x_title)
    mp.ylabel(y_title)
    mp.title(graph_title)

    # Mostrar la leyenda
    mp.legend()

    # Mostrar el gráfico
    mp.grid(True)
    mp.show()

def graphMean(values:pd.DataFrame):
    meanTemp = values.groupby("id_station")["temperature"].mean()
    meanHum = values.groupby("id_station")["humidity"].mean()
    meanWind = values.groupby("id_station")["wind_speed"].mean()
    meanRad = values.groupby("id_station")["solar_radiation"].mean()
    fig, ax = mp.subplots(4,1,figsize=(10, 16))
    
    ax[0].bar(meanTemp.index, meanTemp)
    ax[0].set_xlabel("Estacion")
    ax[0].set_ylabel("Temperatura(C°)")
    ax[0].set_title("Media de Temperaturas")
    ax[1].bar(meanHum.index, meanHum)
    ax[1].set_xlabel("Estacion")
    ax[1].set_ylabel("Humedad(%)")
    ax[1].set_title("Media de Humedad")
    ax[2].bar(meanWind.index, meanWind)
    ax[2].set_xlabel("Estacion")
    ax[2].set_ylabel("Velocidad del Viento(km/h)")
    ax[2].set_title("Media de Velocidad del Viento")
    ax[3].bar(meanRad.index, meanRad)
    ax[3].set_xlabel("Estacion")
    ax[3].set_ylabel("Radiacion Solar(%)")
    ax[3].set_title("Media de Radiacion Solar")
    fig.tight_layout()
    fig.subplots_adjust(hspace=0.5)
    fig.show()

def graphMax(values:pd.DataFrame):
    meanTemp = values.groupby("id_station")["temperature"].max()
    meanHum = values.groupby("id_station")["humidity"].max()
    meanWind = values.groupby("id_station")["wind_speed"].max()
    meanRad = values.groupby("id_station")["solar_radiation"].max()
    fig, ax = mp.subplots(4,1,figsize=(10, 16))
    
    ax[0].bar(meanTemp.index, meanTemp)
    ax[0].set_xlabel("Estacion")
    ax[0].set_ylabel("Temperatura(C°)")
    ax[0].set_title("Maxima de Temperaturas")
    ax[1].bar(meanHum.index, meanHum)
    ax[1].set_xlabel("Estacion")
    ax[1].set_ylabel("Humedad(%)")
    ax[1].set_title("Maxima de Humedad")
    ax[2].bar(meanWind.index, meanWind)
    ax[2].set_xlabel("Estacion")
    ax[2].set_ylabel("Velocidad del Viento(km/h)")
    ax[2].set_title("Maxima de Velocidad del Viento")
    ax[3].bar(meanRad.index, meanRad)
    ax[3].set_xlabel("Estacion")
    ax[3].set_ylabel("Radiacion Solar(%)")
    ax[3].set_title("Maxima de Radiacion Solar")
    fig.tight_layout()
    fig.show()

def graphMin(values:pd.DataFrame):
    meanTemp = values.groupby("id_station")["temperature"].min()
    meanHum = values.groupby("id_station")["humidity"].min()
    meanWind = values.groupby("id_station")["wind_speed"].min()
    meanRad = values.groupby("id_station")["solar_radiation"].min()
    fig, ax = mp.subplots(4,1,figsize=(10, 16))
    
    ax[0].bar(meanTemp.index, meanTemp)
    ax[0].set_xlabel("Estacion")
    ax[0].set_ylabel("Temperatura(C°)")
    ax[0].set_title("Minima de Temperaturas")
    ax[1].bar(meanHum.index, meanHum)
    ax[1].set_xlabel("Estacion")
    ax[1].set_ylabel("Humedad(%)")
    ax[1].set_title("Minima de Humedad")
    ax[2].bar(meanWind.index, meanWind)
    ax[2].set_xlabel("Estacion")
    ax[2].set_ylabel("Velocidad del Viento(km/h)")
    ax[2].set_title("Minima de Velocidad del Viento")
    ax[3].bar(meanRad.index, meanRad)
    ax[3].set_xlabel("Estacion")
    ax[3].set_ylabel("Radiacion Solar(%)")
    ax[3].set_title("Minima de Radiacion Solar")
    fig.tight_layout()
    fig.show()
def graph3D(x_values,y_values,z_values, x_title, y_title, z_title, graph_title):
    fig = mp.figure(figsize=(8, 5))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x_values, y_values, z_values, cmap='viridis')
    ax.set_xlabel(x_title)
    ax.set_ylabel(y_title)
    ax.set_zlabel(z_title)
    ax.set_title(graph_title)

    mp.show()

if __name__ == "__main__":
    x = [1,2,3,4,5]
    y = [1,2,3,4,5]
    #graph2D(x,y,"valor X", "valor Y", "Prueba")
    #graph2D(x,list(map(lambda x: x*2, y)),"valor X", "valor Y", "Prueba2")
    #graph3D(x,y,z,"Datos X", "Datos Y","Datos Z","Prueba")

    # Definir la función Z = f(X, Y)
    X,Y = np.meshgrid(x,y)
    Z = X + Y
    graph3D(X,Y,Z, "Datos X", "Datos Y", "Datos Z", "Prueba")