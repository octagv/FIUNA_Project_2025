import sqlite3
import pandas as pd
def getStationPoints():
    conection = sqlite3.connect("db/app_log.db")
    cursor = conection.cursor()
    cursor.execute("SELECT DISTINCT id_station, latitud, longitud FROM logs")
    data = cursor.fetchall()
    conection.close()
    return data
def getAllData():
    con = sqlite3.connect("db/app_log.db")
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