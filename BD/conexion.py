import sqlite3
import os

class DAO:  # Data Access Object
    def __init__(self):
        try:
            ruta_db = os.path.join(os.path.dirname(__file__), 'tienda_videojuegos.db')
            self.conexion = sqlite3.connect(ruta_db)
        except sqlite3.Error as ex:
            print(f'\nError en la conexion: {ex}')
            self.conexion = None
    
    def cerrar_conexion(self):
        if self.conexion:
            self.conexion.close()
            print('Conexion cerrada.')
