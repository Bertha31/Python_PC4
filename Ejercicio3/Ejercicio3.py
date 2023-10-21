import requests
import zipfile
import os

# URL de la imagen
url = 'https://images.unsplash.com/photo-1601979031925-424e53b6caaa?auto=format&fit=crop&q=80&w=2574&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D.jpg'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

directory = "/workspaces/Python_PC4/Ejercicio3"
if not os.path.exists(directory):
    os.makedirs(directory)

respuesta = requests.get(url, headers=headers)

imagen_path = os.path.join(directory, 'perrito.jpg')
with open(imagen_path, 'wb') as f:
    f.write(respuesta.content)

archivo_zip = os.path.join(directory, 'Perro.zip')
with zipfile.ZipFile(archivo_zip, 'w') as zipf:
    zipf.write(imagen_path, 'perrito.jpg')

# Descomprimir el archivo ZIP
unzip_directory = os.path.join(directory, 'unzipped_images')
if not os.path.exists(unzip_directory):
    os.makedirs(unzip_directory)

with zipfile.ZipFile(archivo_zip, 'r') as zipf:
    zipf.extractall(unzip_directory)

os.remove(imagen_path)
