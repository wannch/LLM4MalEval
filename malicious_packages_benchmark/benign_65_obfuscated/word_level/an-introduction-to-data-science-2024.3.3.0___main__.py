from http.server import    SimpleHTTPRequestHandler,    HTTPServer
by=True
bn=len
bJ=int
bM=print
from socketserver import ThreadingMixIn
import sys
bA=sys.argv
from os import path
import os
bQ=os.chdir

class bN(ThreadingMixIn, HTTPServer):
    bx = by

def bX():
    bQ(path.dirname(__file__))
    bl = bA[int("".join([chr(49)]))             ] if bn(bA) >int("".join([chr(49)]))                             elseint("".join([chr(51),chr(48),chr(48),chr(48)]))
    bD = (("".join([chr(108),chr(111),chr(99),chr(97),chr(108),chr(104),chr(111),chr(115),chr(116)]))                     , bJ(bl))
    SimpleHTTPRequestHandler.protocol_version =("".join([chr(72),chr(84),chr(84),chr(80),chr(47),chr(49),chr(46),chr(49)]))
    bj = bN(bD, SimpleHTTPRequestHandler)
    bM(f"Serving HTTP on localhost port {port} ...")
    bj.serve_forever()

if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         : bX()