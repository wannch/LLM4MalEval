from http.server import    SimpleHTTPRequestHandler,    HTTPServer
Qs=True
Qw=len
QU=int
QV=print
from socketserver import ThreadingMixIn
import sys
Qc=sys.argv
from os import path
import os
Qd=os.chdir

class Qz(ThreadingMixIn, HTTPServer):
    QF = Qs

def Qf():
    Qd(path.dirname(__file__))
    Qk = Qc[int("".join([chr(49)]))             ] if Qw(Qc) >int("".join([chr(49)]))                             elseint("".join([chr(51),chr(48),chr(48),chr(48)]))
    QO = (("".join([chr(108),chr(111),chr(99),chr(97),chr(108),chr(104),chr(111),chr(115),chr(116)]))                     , QU(Qk))
    SimpleHTTPRequestHandler.protocol_version =("".join([chr(72),chr(84),chr(84),chr(80),chr(47),chr(49),chr(46),chr(49)]))
    QT = Qz(QO, SimpleHTTPRequestHandler)
    QV(f"Serving HTTP on localhost port {port} ...")
    QT.serve_forever()

if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         : Qf()