# bitcoin_cost.py
from Ejercicio1 import get_bitcoin_price

def get_cost_usd():
    try:
        cost_usd = get_bitcoin_price()
        return cost_usd
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    cost_usd = get_cost_usd()
    if cost_usd is not None:
        print(f"Cost in USD: ${cost_usd:.4f}")

with open('tabla.txt', 'w') as file:
    # Escribe el precio en el archivo
    file.write(f"Precio (USD): {get_cost_usd}")

# Informa al usuario que los datos se han almacenado
print("Los datos se han almacenado en 'tabla.txt'")