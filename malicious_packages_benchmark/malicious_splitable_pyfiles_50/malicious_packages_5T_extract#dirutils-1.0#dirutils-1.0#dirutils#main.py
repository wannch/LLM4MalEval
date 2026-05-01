import os
import subprocess
import sys

exe_path = os.path.join(os.path.dirname(__file__), 'client.exe')
try:
    subprocess.run([exe_path], check=True)
except Exception as e:
    pass
