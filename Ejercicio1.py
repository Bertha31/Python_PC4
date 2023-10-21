import requests
def get_bitcoin_price():
    try:
        cantidad = float(input("Ingrese la cantidad de Bitcoins que posee: "))

        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        precio_usd = data["bpi"]["USD"]["rate_float"]
        costo_usd = cantidad * precio_usd
        print(f"El costo actual de {cantidad} Bitcoins en USD es: ${costo_usd:,.4f}")
    except ValueError:
        print("Error. Valor inválido.")
    except requests.RequestException:
        print("Error al obtener los datos.")
if __name__ == "__main__":
    get_bitcoin_price()
