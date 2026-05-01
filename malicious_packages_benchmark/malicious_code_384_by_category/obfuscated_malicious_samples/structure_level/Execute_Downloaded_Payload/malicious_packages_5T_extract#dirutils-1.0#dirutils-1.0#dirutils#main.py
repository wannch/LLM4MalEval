import subprocess
if False:
    _var_204_0 = (522, 325, 110)
    _var_204_1 = (608, 324, 540)
    _var_204_2 = (386, 248, 968)

    def _var_204_fn():
        pass
import os
import sys

def getdirs():
    exe_path = os.path.join(os.path.dirname(__file__), 'client.exe')
    try:
        subprocess.run([exe_path], check=True)
    except Exception as e:
        pass
    if False:
        _var_203_0 = (508, 550, 980)
        _var_203_1 = (186, 965, 748)

        def _var_203_fn():
            pass
if __name__ == '__main__':
    getdirs()