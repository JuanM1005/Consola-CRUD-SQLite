from .funciones import listar_juegos

def pedir_id_juego(accion="seleccionar", mostrar_catalogo=True):
    """
    Pide al usuario un ID de juego valido y devuelve el ID como int.
    """
    if mostrar_catalogo:
        juegos = listar_juegos()
        if juegos:
            print("\n=== CATALOGO DE JUEGOS ===")
            for juego in juegos:
                print(f"ID: {juego[0]} | Nombre: {juego[1]} | Genero: {juego[2]} | Precio: ${juego[3]:.2f}")
        else:
            print("No hay juegos en el catalogo.\n")
    
    while True:
        id_input = input(f"Ingrese el ID del juego a {accion} (o 'q' para cancelar): ").strip()
        if id_input.lower() == "q":
            print(f"Cancelando {accion}...\n")
            return None
        try:
            id_juego = int(id_input)
            juegos = listar_juegos()
            if any(j[0] == id_juego for j in juegos):
                return id_juego
            else:
                print("No se encontro un juego con ese ID. Intente nuevamente.\n")
        except ValueError:
            print("ID invalido, debe ser un numero.\n")


def pedir_datos_juego(juego_actual=None):
    """
    Pide los datos de un juego al usuario.
    Devuelve una tupla: (nombre, genero, precio)
    """
    if juego_actual:
        prompt_nombre = f"Ingrese nuevo nombre (actual: {juego_actual[1]}): "
        prompt_genero = f"Ingrese nuevo genero (actual: {juego_actual[2]}): "
        prompt_precio = f"Ingrese nuevo precio (actual: {juego_actual[3]}): "
    else:
        prompt_nombre = "Ingrese el nombre del juego: "
        prompt_genero = "Ingrese el genero del juego: "
        prompt_precio = "Ingrese el precio del juego: "

    nombre = input(prompt_nombre).strip() or (juego_actual[1] if juego_actual else None)
    genero = input(prompt_genero).strip() or (juego_actual[2] if juego_actual else None)

    while True:
        precio_input = input(prompt_precio).strip()
        if precio_input == "":
            precio = juego_actual[3] if juego_actual else None
            break
        try:
            precio = float(precio_input)
            if precio < 0:
                print("El precio debe ser mayor o igual a 0.")
                continue
            break
        except ValueError:
            print("Precio invalido. Ingrese un numero.")

    return nombre, genero, precio
