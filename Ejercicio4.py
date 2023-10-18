# Datos de precios de Bitcoin
bitcoin_prices = [50000.12, 51000.23, 51500.45, 52000.67, 52500.78]

# Nombre del archivo de salida
output_file = 'tabla.txt'

# Abre el archivo para escritura
with open(output_file, 'w') as file:
    file.write("Fecha\tPrecio (USD)\n")  # Encabezado

    # Escribe los datos en el archivo con el formato adecuado
    for i, price in enumerate(bitcoin_prices, start=1):
        file.write(f"2023-10-18\t{price:.2f}\n")  # Cambia la fecha por la fecha real

print(f"Los datos se han almacenado en {output_file}")
