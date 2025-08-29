from funciones.funciones import *
from funciones.funciones_auxiliares import *

def menu_principal():
    while True:
        print("=== TIENDA DE VIDEOJUEGOS ===\n"
              "1. Ver catalogo de juegos\n"
              "2. Agregar nuevo juego al inventario\n"
              "3. Eliminar un juego del inventario\n"
              "4. Actualizar informacion de un juego\n"
              "5. Salir de la tienda")
        try:
            opcion = int(input("Ingrese su opcion: "))
        except ValueError:
            print("Opcion invalida, ingrese un numero del 1 al 5.\n")
            continue

        if opcion < 1 or opcion > 5:
            print("Opcion incorrecta, ingrese nuevamente\n")
        elif opcion == 5:
            print("Saliendo de la tienda...")
            break
        else:
            ejecutar_opcion(opcion)

def ejecutar_opcion(opcion):
    match opcion:

        case 1:  # Mostrar catalogo
            try:
                juegos = listar_juegos()
                if juegos:
                    print('\n=== CATALOGO DE JUEGOS ===\n')
                    for juego in juegos:
                        print(f"ID: {juego[0]} | Nombre: {juego[1]} | Genero: {juego[2]} | Precio: ${juego[3]:.2f}")
                else:
                    print("No hay juegos en el catalogo.")
            except Exception as ex:
                print(f"Ocurrio un error: {ex}")
            finally:
                print('\n')

        case 2:  # Agregar juego
            print("\n=== AGREGAR NUEVO JUEGO AL INVENTARIO ===")
            try:
                nombre, genero, precio = pedir_datos_juego()
                if nombre and genero and precio is not None:
                    if insertar_juego(nombre, genero, precio):
                        print("Juego agregado correctamente.\n")
                    else:
                        print("Error al agregar el juego.\n")
                else:
                    print("No se proporcionaron todos los datos. Operacion cancelada.\n")
            except Exception as ex:
                print(f"Ocurrio un error: {ex}")

        case 3:  # Eliminar juego
            print("\n=== ELIMINAR UN JUEGO DEL INVENTARIO ===")
            try:
                id_juego = pedir_id_juego("eliminar")
                if id_juego is not None:
                    if eliminar_juego(id_juego):
                        print("Juego eliminado correctamente.\n")
                    else:
                        print("No se encontro ningun juego con ese ID.\n")
            except Exception as ex:
                print(f"Ocurrio un error: {ex}")

        case 4:  # Actualizar juego
            print("\n=== ACTUALIZAR INFORMACION DE UN JUEGO ===")
            try:
                id_juego = pedir_id_juego("actualizar")
                if id_juego:
                    juegos = listar_juegos()
                    juego_actual = next((j for j in juegos if j[0] == id_juego), None)
                    if not juego_actual:
                        print("No se encontro ningun juego con ese ID.\n")
                        return

                    nombre, genero, precio = pedir_datos_juego(juego_actual)
                    if actualizar_juego(id_juego, nombre, genero, precio):
                        print("Juego actualizado correctamente.\n")
                    else:
                        print("No se realizaron cambios.\n")
            except Exception as ex:
                print(f"Ocurrio un error: {ex}")