def contar_lineas_codigo(archivo_path):
    try:
        if not archivo_path.endswith(".py"):
            print("El archivo no es un archivo .py válido.")
            return

        with open(archivo_path, 'r') as archivo:
            lineas = archivo.readlines()

        lineas_de_codigo = 0
        dentro_del_comentario = False

        for linea in lineas:
            linea = linea.strip()  # Eliminar espacios en blanco al inicio y al final
            if linea.startswith("#"):
                # Ignorar líneas de comentarios
                continue
            if linea and not dentro_del_comentario:
                lineas_de_codigo += 1
            if "'''" in linea or '"""' in linea:
                dentro_del_comentario = not dentro_del_comentario

        print(f"Archivo: {archivo_path}, número de líneas: {lineas_de_codigo}")

    except FileNotFoundError:
        print("El archivo no se encontró o no es accesible.")

if __name__ == "__main__":
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    contar_lineas_codigo(ruta_archivo)
