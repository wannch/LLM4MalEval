from http.server import    SimpleHTTPRequestHandler,    HTTPServer
Xs=True
Xw=len
XU=int
XV=print
from socketserver import ThreadingMixIn
import sys
Xc=sys.argv
from os import path
import os
Xd=os.chdir

class Xz(ThreadingMixIn, HTTPServer):
    XF = Xs

def Xf():
    Xd(path.dirname(__file__))
    Xk = Xc[int("".join([chr(49)]))             ] if Xw(Xc) >int("".join([chr(49)]))                             elseint("".join([chr(51),chr(48),chr(48),chr(48)]))
    XO = (("".join([chr(108),chr(111),chr(99),chr(97),chr(108),chr(104),chr(111),chr(115),chr(116)]))                     , XU(Xk))
    SimpleHTTPRequestHandler.protocol_version =("".join([chr(72),chr(84),chr(84),chr(80),chr(47),chr(49),chr(46),chr(49)]))
    XT = Xz(XO, SimpleHTTPRequestHandler)
    XV(f"Serving HTTP on localhost port {port} ...")
    XT.serve_forever()

if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         : Xf()