import sqlite3
from sqlite3 import Error


ubicacionBD = "./db/database.db"


def crear_conexion(rutaBD=ubicacionBD):
    objeto_conexion = None
    try:
        objeto_conexion = sqlite3.connect(rutaBD)
    except Error as e:
        print("||||||||||||||||||||||||||||")
        print("Error de conexión con la BD")
        print(f"{e}\n")
        print("||||||||||||||||||||||||||||")

    return objeto_conexion
