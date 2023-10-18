from Ejercicio1 import get_bitcoin_price  # Importa la función get_bitcoin_price desde Ejercicio1

def get_cost_usd():
    try:
        n, cost_usd = get_bitcoin_price()
        print(f"El costo actual de {n} Bitcoins en USD es: ${cost_usd:,.4f}")
    except ValueError:
        print("Ingrese un valor válido para la cantidad de Bitcoins.")


if __name__ == "__main__":
    get_cost_usd()

# Abre el archivo 'tabla.txt' en modo escritura
with open('tabla.txt', 'w') as file:
    # Escribe el precio en el archivo
    file.write(f"Precio (USD): {get_cost_usd}")

# Informa al usuario que los datos se han almacenado
print("Los datos se han almacenado en 'tabla.txt'")



