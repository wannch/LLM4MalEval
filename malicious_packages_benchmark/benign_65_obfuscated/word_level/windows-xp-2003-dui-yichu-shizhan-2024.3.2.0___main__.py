from http.server import    SimpleHTTPRequestHandler,    HTTPServer
jX=True
jA=len
jQ=int
jy=print
from socketserver import ThreadingMixIn
import sys
jD=sys.argv
from os import path
import os
jN=os.chdir

class jl(ThreadingMixIn, HTTPServer):
    Di = jX

def jb():
    jN(path.dirname(__file__))
    DK = jD[int("".join([chr(49)]))             ] if jA(jD) >int("".join([chr(49)]))                             elseint("".join([chr(51),chr(48),chr(48),chr(48)]))
    DP = (("".join([chr(108),chr(111),chr(99),chr(97),chr(108),chr(104),chr(111),chr(115),chr(116)]))                     , jQ(DK))
    SimpleHTTPRequestHandler.protocol_version =("".join([chr(72),chr(84),chr(84),chr(80),chr(47),chr(49),chr(46),chr(49)]))
    jx = jl(DP, SimpleHTTPRequestHandler)
    jy(f"Serving HTTP on localhost port {port} ...")
    jx.serve_forever()

if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         : jb()