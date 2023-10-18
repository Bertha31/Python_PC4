import requests

def get_bitcoin_price():
    try:
        # Solicita al usuario la cantidad de Bitcoins que posee
        n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
        
        # Consulta la API de CoinDesk para obtener el precio actual de Bitcoin en USD
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        price_usd = data["bpi"]["USD"]["rate_float"]

        # Calcula el costo actual en USD de los Bitcoins que posee el usuario
        cost_usd = n * price_usd

        # Muestra el costo actual con cuatro decimales y usando "," como separador de miles
        print(f"El costo actual de {n} Bitcoins en USD es: ${cost_usd:,.4f}")
        
        # Abre un archivo para escritura y guarda el resultado en el archivo txt
        file_path = "/workspaces/Python_PC4/Ejercicio4/tabla.txt"
        with open(file_path, 'w') as file:
            file.write(f"Precio (USD): {cost_usd:,.4f}")

    except ValueError:
        print("Ingrese un valor válido para la cantidad de Bitcoins.")
    except requests.RequestException:
        print("Error al obtener los datos de CoinDesk.")

if __name__ == "__main__":
    get_bitcoin_price()




