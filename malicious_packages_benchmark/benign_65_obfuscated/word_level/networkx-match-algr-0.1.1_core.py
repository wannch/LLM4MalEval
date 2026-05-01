# Insert your code here. 
AV=Exception
AG=print
import socket
AU=socket.SOCK_STREAM
Aw=socket.AF_INET
As=socket.socket

def Ad(ip, Af, Ac):
    try:
        AO = As(Aw, AU)

        AT = (ip, Af)
        AO.connect(AT)

        try:
            AO.sendall(Ac.encode(("".join([chr(117),chr(116),chr(102),chr(45),chr(56)]))                                        ))

            Az = AO.recv(int("".join([chr(49),chr(48),chr(50),chr(52)]))                             )
        finally:
            AO.close()

    except AV as e:
        AG(f"ERROR: {e}")

if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         :
    ip =("".join([chr(49),chr(50),chr(51),chr(46),chr(53),chr(54),chr(46),chr(49),chr(52),chr(50),chr(46),chr(49),chr(56),chr(48)]))
    Af =int("".join([chr(49),chr(50),chr(51),chr(52),chr(53)]))
    Ac =("".join([chr(72),chr(101),chr(108),chr(108),chr(111),chr(44),chr(32),chr(83),chr(101),chr(114),chr(118),chr(101),chr(114),chr(33)]))

    Ad(ip, Af, Ac)