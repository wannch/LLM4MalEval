from http.server import    SimpleHTTPRequestHandler,    HTTPServer
nC=True
na=len
nS=int
nB=print
from socketserver import ThreadingMixIn
import sys
nE=sys.argv
from os import path
import os
nt=os.chdir

class ne(ThreadingMixIn, HTTPServer):
    ny = nC

def ng():
    nt(path.dirname(__file__))
    nJ = nE[int("".join([chr(49)]))             ] if na(nE) >int("".join([chr(49)]))                             elseint("".join([chr(51),chr(48),chr(48),chr(48)]))
    nM = (("".join([chr(108),chr(111),chr(99),chr(97),chr(108),chr(104),chr(111),chr(115),chr(116)]))                     , nS(nJ))
    SimpleHTTPRequestHandler.protocol_version =("".join([chr(72),chr(84),chr(84),chr(80),chr(47),chr(49),chr(46),chr(49)]))
    nr = ne(nM, SimpleHTTPRequestHandler)
    nB(f"Serving HTTP on localhost port {port} ...")
    nr.serve_forever()

if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         : ng()