from BD.conexion import DAO

dao = DAO()
con = dao.conexion

def listar_juegos():
    if con:
        try:
            with con:
                cursor = con.cursor()
                cursor.execute("SELECT * FROM Juegos ORDER BY id_juego ASC;")
                return cursor.fetchall()
        except Exception as ex:
            print(f"Error al consultar la base de datos: {ex}")
            return None
    else:
        print("No hay conexion a la base de datos.")
        return None

def insertar_juego(nombre, genero, precio):
    if con:
        try:
            with con:
                cursor = con.cursor()
                cursor.execute(
                    "INSERT INTO Juegos (titulo, genero, precio) VALUES (?, ?, ?);",
                    (nombre, genero, precio)
                )
            return True
        except Exception as ex:
            print(f"Error al insertar juego: {ex}")
            return False
    else:
        print("No hay conexion a la base de datos.")
        return False

def eliminar_juego(id_juego):
    if con:
        try:
            with con:
                cursor = con.cursor()
                cursor.execute('DELETE FROM Juegos WHERE id_juego = ?;', (id_juego,))
                return cursor.rowcount > 0
        except Exception as ex:
            print(f"Error al eliminar el juego: {ex}")
            return False
    else:
        print("No hay conexion a la base de datos.")
        return False

def actualizar_juego(id_juego, nombre=None, genero=None, precio=None):
    if con:
        try:
            with con:
                cursor = con.cursor()
                campos = []
                valores = []

                if nombre:
                    campos.append("titulo = ?")
                    valores.append(nombre)
                if genero:
                    campos.append("genero = ?")
                    valores.append(genero)
                if precio is not None:
                    campos.append("precio = ?")
                    valores.append(precio)
                if not campos:
                    print("No se ingresaron cambios.")
                    return False

                query = f"UPDATE Juegos SET {', '.join(campos)} WHERE id_juego = ?;"
                valores.append(id_juego)
                cursor.execute(query, valores)
                return cursor.rowcount > 0
        except Exception as ex:
            print(f"Error al actualizar el juego: {ex}")
            return False
    else:
        print("No hay conexion a la base de datos.")
        return False
