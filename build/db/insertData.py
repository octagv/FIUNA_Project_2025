import sqlite3
import pandas as pd
def insertEntry(data):
    conection = sqlite3.connect("build/db/app_log.db")
    cursor = conection.cursor()
    cursor.execute("INSERT INTO logs (time, id_station, latitud, longitud, temperature, humidity, wind_speed, solar_radiation) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
    data)
    conection.commit()
    conection.close() 

def insertDatafromCsv(csv):
    table = pd.read_csv(csv,header=None, sep=";")
    conection = sqlite3.connect("build/db/app_log.db")
    cursor = conection.cursor()
    for line in table.itertuples(index=False):
        cursor.execute("INSERT INTO logs (time, id_station, latitud, longitud, temperature, humidity, wind_speed, solar_radiation) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       line)
    conection.commit()
    conection.close()

if __name__ == "__main__":
    data = (
        100,
        1,
        100,
        100,
        35,
        80,
        22,
        34
    )
    #insertEntry(data)
    #insertDatafromCsv("Libro1.csv")