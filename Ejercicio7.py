import requests
import sqlite3

# URL de la API de SUNAT
url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'

# Realizar una solicitud a la API de SUNAT
response = requests.get(url)


if response.status_code == 200:

    data = response.json()

    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sunat_info (
            fecha TEXT PRIMARY KEY,
            compra REAL,
            venta REAL
        )
    ''')

    for entry in data:
        fecha = entry['fecha']
        compra = entry['compra']
        venta = entry['venta']
        cursor.execute('''
            INSERT OR REPLACE INTO sunat_info (fecha, compra, venta)
            VALUES (?, ?, ?)
        ''', (fecha, compra, venta))

    conn.commit()
    conn.close()

    print("Datos almacenados en la tabla 'sunat_info'.")

else:
    print("Error al conectarse a la API de SUNAT. Código de estado:", response.status_code)
