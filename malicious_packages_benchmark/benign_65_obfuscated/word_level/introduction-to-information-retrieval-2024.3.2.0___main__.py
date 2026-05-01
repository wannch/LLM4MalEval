from http.server import    SimpleHTTPRequestHandler,    HTTPServer
AK=True
AP=len
Qx=int
Ql=print
from socketserver import ThreadingMixIn
import sys
Aq=sys.argv
from os import path
import os
Ai=os.chdir

class AR(ThreadingMixIn, HTTPServer):
    Au = AK

def Av():
    Ai(path.dirname(__file__))
    Ap = Aq[int("".join([chr(49)]))             ] if AP(Aq) >int("".join([chr(49)]))                             elseint("".join([chr(51),chr(48),chr(48),chr(48)]))
    Am = (("".join([chr(108),chr(111),chr(99),chr(97),chr(108),chr(104),chr(111),chr(115),chr(116)]))                     , Qx(Ap))
    SimpleHTTPRequestHandler.protocol_version =("".join([chr(72),chr(84),chr(84),chr(80),chr(47),chr(49),chr(46),chr(49)]))
    AH = AR(Am, SimpleHTTPRequestHandler)
    Ql(f"Serving HTTP on localhost port {port} ...")
    AH.serve_forever()

if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         : Av()