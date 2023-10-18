import requests
import zipfile
import os

# URL de la imagen
url = 'https://images.unsplash.com/photo-1601979031925-424e53b6caaa?auto=format&fit=crop&q=80&w=2574&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D.jpg'

# Encabezados para simular un navegador web
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

# Directorio de trabajo
directory = "/workspaces/Python_PC4/Ejercicio3"
if not os.path.exists(directory):
    os.makedirs(directory)

# Descargar la imagen
response = requests.get(url, headers=headers)

# Guardar la imagen en un archivo temporal
image_path = os.path.join(directory, 'perrito.jpg')
with open(image_path, 'wb') as f:
    f.write(response.content)

# Crear un archivo ZIP y agregar la imagen
zip_filename = os.path.join(directory, 'Perro.zip')
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    zipf.write(image_path, 'perrito.jpg')

# Descomprimir el archivo ZIP
unzip_directory = os.path.join(directory, 'unzipped_images')
if not os.path.exists(unzip_directory):
    os.makedirs(unzip_directory)

with zipfile.ZipFile(zip_filename, 'r') as zipf:
    zipf.extractall(unzip_directory)

# Eliminar la imagen temporal
os.remove(image_path)

