import sqlite3

def createDb():
    conection = sqlite3.connect("build/db/app_log.db")
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