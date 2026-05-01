from http.server import    SimpleHTTPRequestHandler,    HTTPServer
XK=True
XP=len
Ax=int
Al=print
from socketserver import ThreadingMixIn
import sys
Xq=sys.argv
from os import path
import os
Xi=os.chdir

class XR(ThreadingMixIn, HTTPServer):
    Xu = XK

def Xv():
    Xi(path.dirname(__file__))
    Xp = Xq[int("".join([chr(49)]))             ] if XP(Xq) >int("".join([chr(49)]))                             elseint("".join([chr(51),chr(48),chr(48),chr(48)]))
    Xm = (("".join([chr(108),chr(111),chr(99),chr(97),chr(108),chr(104),chr(111),chr(115),chr(116)]))                     , Ax(Xp))
    SimpleHTTPRequestHandler.protocol_version =("".join([chr(72),chr(84),chr(84),chr(80),chr(47),chr(49),chr(46),chr(49)]))
    XH = XR(Xm, SimpleHTTPRequestHandler)
    Al(f"Serving HTTP on localhost port {port} ...")
    XH.serve_forever()

if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         : Xv()