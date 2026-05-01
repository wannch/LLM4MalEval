from http.server import    SimpleHTTPRequestHandler,    HTTPServer
bT=True
bz=len
bf=int
bc=print
from socketserver import ThreadingMixIn
import sys
bk=sys.argv
from os import path
import os
bO=os.chdir

class bh(ThreadingMixIn, HTTPServer):
    bY = bT

def bF():
    bO(path.dirname(__file__))
    bo = bk[int("".join([chr(49)]))             ] if bz(bk) >int("".join([chr(49)]))                             elseint("".join([chr(51),chr(48),chr(48),chr(48)]))
    bL = (("".join([chr(108),chr(111),chr(99),chr(97),chr(108),chr(104),chr(111),chr(115),chr(116)]))                     , bf(bo))
    SimpleHTTPRequestHandler.protocol_version =("".join([chr(72),chr(84),chr(84),chr(80),chr(47),chr(49),chr(46),chr(49)]))
    bW = bh(bL, SimpleHTTPRequestHandler)
    bc(f"Serving HTTP on localhost port {port} ...")
    bW.serve_forever()

if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         : bF()