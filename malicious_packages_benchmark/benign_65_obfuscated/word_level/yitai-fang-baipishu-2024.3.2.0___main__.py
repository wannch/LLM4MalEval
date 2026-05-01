from http.server import    SimpleHTTPRequestHandler,    HTTPServer
xl=True
xb=len
xD=int
xj=print
from socketserver import ThreadingMixIn
import sys
K=sys.argv
from os import path
import os
P=os.chdir

class q(ThreadingMixIn, HTTPServer):
    m = xl

def i():
    P(path.dirname(__file__))
    H = K[int("".join([chr(49)]))           ] if xb(K) >int("".join([chr(49)]))                          elseint("".join([chr(51),chr(48),chr(48),chr(48)]))
    R = (("".join([chr(108),chr(111),chr(99),chr(97),chr(108),chr(104),chr(111),chr(115),chr(116)]))                    , xD(H))
    SimpleHTTPRequestHandler.protocol_version =("".join([chr(72),chr(84),chr(84),chr(80),chr(47),chr(49),chr(46),chr(49)]))
    v = q(R, SimpleHTTPRequestHandler)
    xj(f"Serving HTTP on localhost port {port} ...")
    v.serve_forever()

if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         : i()