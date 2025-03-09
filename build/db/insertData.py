import sqlite3

def insertEntry(data):
    conection = sqlite3.connect("build/db/app_log.db")
    cursor = conection.cursor()
    cursor.execute("INSERT INTO logs (time, id_station, latitud, longitud, temperature, humidity, wind_speed, solar_radiation) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
    (data["time"], data["id"], data["lat"], data["lon"], data["temp"], data["hum"], data["wind"], data["rad"]))
    conection.commit()
    conection.close() 

if __name__ == "__main__":
    data = {
        "time":100,
        "id": 1,
        "lat": 100,
        "lon": 100,
        "temp": 35,
        "hum": 80,
        "wind": 22,
        "rad": 34
    }
    insertEntry(data)