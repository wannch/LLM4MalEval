from http.server import    SimpleHTTPRequestHandler,    HTTPServer
lx=True
lb=len
lD=int
lj=print
from socketserver import ThreadingMixIn
import sys
xK=sys.argv
from os import path
import os
xP=os.chdir

class xq(ThreadingMixIn, HTTPServer):
    xm = lx

def xi():
    xP(path.dirname(__file__))
    xH = xK[int("".join([chr(49)]))             ] if lb(xK) >int("".join([chr(49)]))                             elseint("".join([chr(51),chr(48),chr(48),chr(48)]))
    xR = (("".join([chr(108),chr(111),chr(99),chr(97),chr(108),chr(104),chr(111),chr(115),chr(116)]))                     , lD(xH))
    SimpleHTTPRequestHandler.protocol_version =("".join([chr(72),chr(84),chr(84),chr(80),chr(47),chr(49),chr(46),chr(49)]))
    xv = xq(xR, SimpleHTTPRequestHandler)
    lj(f"Serving HTTP on localhost port {port} ...")
    xv.serve_forever()

if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         : xi()