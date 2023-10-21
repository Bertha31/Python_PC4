import os  

def guardar_tabla_multiplicar(numero):
    # Define la ruta completa del archivo
    archivo = os.path.join("/workspaces/Python_PC4/Ejercicio5", f'tabla-{numero}.txt')
    with open(archivo, 'w') as file:
        for i in range(1, 11):
            file.write(f'{numero} x {i} = {numero * i}\n')

def mostrar_tabla(numero):
    try:
        # Define la ruta completa del archivo
        archivo = os.path.join("/workspaces/Python_PC4/Ejercicio5", f'tabla-{numero}.txt')
        with open(archivo, 'r') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def mostrar_linea_tabla(numero, linea):
    try:
        archivo = os.path.join("/workspaces/Python_PC4/Ejercicio5", f'tabla-{numero}.txt')
        with open(archivo, 'r') as file:
            lines = file.readlines()
            if linea <= len(lines):
                print(lines[linea - 1], end='')
            else:
                print(f"La línea {linea} no existe en la tabla de multiplicar de {numero}.")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

# Menú principal
while True:
    print("Menú:")
    print("1. Guardar tabla de multiplicar en un archivo")
    print("2. Mostrar tabla de multiplicar")
    print("3. Mostrar línea de la tabla de multiplicar")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1/2/3/4): ")
    
    if opcion == "1":
        numero = int(input("Ingrese un número entre 1 y 10: "))
        if 1 <= numero <= 10:
            guardar_tabla_multiplicar(numero)
            print(f"Tabla de multiplicar de {numero} guardada en /workspaces/Python_PC4/Ejercicio5/tabla-{numero}.txt")
        else:
            print("El número debe estar entre 1 y 10.")
    elif opcion == "2":
        numero = int(input("Ingrese un número entre 1 y 10: "))
        if 1 <= numero <= 10:
            mostrar_tabla(numero)
        else:
            print("El número debe estar entre 1 y 10.")
    elif opcion == "3":
        numero = int(input("Ingrese un número entre 1 y 10: "))
        linea = int(input("Ingrese el número de línea que desea ver: "))
        if 1 <= numero <= 10:
            mostrar_linea_tabla(numero, linea)
        else:
            print("El número debe estar entre 1 y 10.")
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Seleccione una opción válida (1/2/3/4).")

