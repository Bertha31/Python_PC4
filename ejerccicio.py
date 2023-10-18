import requests
import os
import zipfile

# URL de la imagen
url = 'https://images.unsplash.com/photo-1601979031925-424e53b6caaa?auto=format&fit=crop&q=80&w=2574&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D.jpg'

# Encabezados para simular un navegador web
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

# Carpeta temporal para almacenar la imagen
temp_dir = 'temp'
os.makedirs(temp_dir, exist_ok=True)

# Guardar la imagen en la carpeta temporal
with open(os.path.join(temp_dir, 'perritoooo.jpg'), 'wb') as f:
    f.write(response.content)

# Comprimir la carpeta temporal en un archivo ZIP
with zipfile.ZipFile('archivos.zip', 'w', zipfile.ZIP_DEFLATED) as zip:
    for foldername, subfolders, filenames in os.walk(temp_dir):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            rel_path = os.path.relpath(file_path, temp_dir)
            zip.write(file_path, rel_path)

# Eliminar la carpeta temporal (opcional)
import shutil
shutil.rmtree(temp_dir)

# Ahora, para extraer la imagen del archivo ZIP
with zipfile.ZipFile('archivos.zip', 'r') as zip:
    zip.extractall('extracted')

# Esto extraerá el archivo en una carpeta llamada 'extracted'.
