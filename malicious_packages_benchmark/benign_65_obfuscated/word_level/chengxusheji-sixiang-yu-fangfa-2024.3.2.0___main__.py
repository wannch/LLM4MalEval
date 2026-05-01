from http.server import    SimpleHTTPRequestHandler,    HTTPServer
Xx=True
Xl=len
Xb=int
XD=print
from socketserver import ThreadingMixIn
import sys
NK=sys.argv
from os import path
import os
NP=os.chdir

class Nq(ThreadingMixIn, HTTPServer):
    Nm = Xx

def Ni():
    NP(path.dirname(__file__))
    NH = NK[int("".join([chr(49)]))             ] if Xl(NK) >int("".join([chr(49)]))                             elseint("".join([chr(51),chr(48),chr(48),chr(48)]))
    NR = (("".join([chr(108),chr(111),chr(99),chr(97),chr(108),chr(104),chr(111),chr(115),chr(116)]))                     , Xb(NH))
    SimpleHTTPRequestHandler.protocol_version =("".join([chr(72),chr(84),chr(84),chr(80),chr(47),chr(49),chr(46),chr(49)]))
    Nv = Nq(NR, SimpleHTTPRequestHandler)
    XD(f"Serving HTTP on localhost port {port} ...")
    Nv.serve_forever()

if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         : Ni()