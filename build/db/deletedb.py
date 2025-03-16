import sqlite3
"""Funcion para eliminar la Tabla"""
def deleteDb():
    conection = sqlite3.connect("db/app_log.db")
    cursor = conection.cursor()

    cursor.execute('''DROP TABLE IF EXISTS logs''')

    conection.commit()
    conection.close()

if __name__ == "__main__":
    deleteDb()
    print("Se elimino correctamente")