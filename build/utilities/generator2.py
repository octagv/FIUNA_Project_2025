import pandas as pd
import numpy as np

def generar_datos_meteorologicos(initial_id, estacion_id, temp_media, humedad_media, viento_media, radiacion_media, num_filas=100):
    # Definir el rango de variación para cada parámetro
    variacion_temp = 3        # ±3 °C
    variacion_humedad = 10    # ±10 %
    variacion_viento = 2      # ±2 km/h
    variacion_radiacion = 10  # ±10 %

    # Generar datos aleatorios alrededor de los valores medios
    temperaturas = np.random.normal(loc=temp_media, scale=variacion_temp, size=num_filas).round(2)
    humedades = np.random.normal(loc=humedad_media, scale=variacion_humedad, size=num_filas).round(2)
    vientos = np.random.normal(loc=viento_media, scale=variacion_viento, size=num_filas).round(2)
    radiaciones = np.random.normal(loc=radiacion_media, scale=variacion_radiacion, size=num_filas).round(2)

    # Limitar los valores a un rango realista (ej: 0–100 % para humedad y radiación)
    humedades = np.clip(humedades, 0, 100)
    radiaciones = np.clip(radiaciones, 0, 100)
    base_time = 1704078000
    times = [base_time + (i * 86400) for i in range(num_filas)]
    # Crear DataFrame
    datos = pd.DataFrame({
        'id': [initial_id + i for i in range(num_filas)],
        'time':times,
        'id_estacion': [estacion_id] * num_filas,
        'temperature': temperaturas,
        'humidity': humedades,
        'wind': vientos,
        'solar_radiation': radiaciones
    })

    return datos

# Ejemplo de uso
if __name__ == "__main__":
    initial_id = 1
    estacion_id = 1
    temp_media = 22.5
    humedad_media = 65
    viento_media = 15
    radiacion_media = 70
    num_filas = 365

    tabla = generar_datos_meteorologicos(initial_id, estacion_id, temp_media, humedad_media, viento_media, radiacion_media, num_filas)
    tabla.to_csv("./build/utilities/dataset/datos_meteorologicos1.csv", index=False)