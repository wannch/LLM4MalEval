from http.server import    SimpleHTTPRequestHandler,    HTTPServer
lr=True
le=len
lg=int
lE=print
from socketserver import ThreadingMixIn
import sys
lJ=sys.argv
from os import path
import os
lM=os.chdir

class ly(ThreadingMixIn, HTTPServer):
    lN = lr

def ln():
    lM(path.dirname(__file__))
    lX = lJ[int("".join([chr(49)]))             ] if le(lJ) >int("".join([chr(49)]))                             elseint("".join([chr(51),chr(48),chr(48),chr(48)]))
    lA = (("".join([chr(108),chr(111),chr(99),chr(97),chr(108),chr(104),chr(111),chr(115),chr(116)]))                     , lg(lX))
    SimpleHTTPRequestHandler.protocol_version =("".join([chr(72),chr(84),chr(84),chr(80),chr(47),chr(49),chr(46),chr(49)]))
    lQ = ly(lA, SimpleHTTPRequestHandler)
    lE(f"Serving HTTP on localhost port {port} ...")
    lQ.serve_forever()

if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         : ln()