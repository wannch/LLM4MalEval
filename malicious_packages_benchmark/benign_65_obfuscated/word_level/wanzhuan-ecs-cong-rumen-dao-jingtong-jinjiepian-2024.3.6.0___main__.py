from http.server import    SimpleHTTPRequestHandler,    HTTPServer
yq=True
yi=len
yK=int
yP=print
from socketserver import ThreadingMixIn
import sys
yR=sys.argv
from os import path
import os
yv=os.chdir

class ym(ThreadingMixIn, HTTPServer):
    yV = yq

def yH():
    yv(path.dirname(__file__))
    yG = yR[int("".join([chr(49)]))             ] if yi(yR) >int("".join([chr(49)]))                             elseint("".join([chr(51),chr(48),chr(48),chr(48)]))
    yu = (("".join([chr(108),chr(111),chr(99),chr(97),chr(108),chr(104),chr(111),chr(115),chr(116)]))                     , yK(yG))
    SimpleHTTPRequestHandler.protocol_version =("".join([chr(72),chr(84),chr(84),chr(80),chr(47),chr(49),chr(46),chr(49)]))
    yp = ym(yu, SimpleHTTPRequestHandler)
    yP(f"Serving HTTP on localhost port {port} ...")
    yp.serve_forever()

if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         : yH()