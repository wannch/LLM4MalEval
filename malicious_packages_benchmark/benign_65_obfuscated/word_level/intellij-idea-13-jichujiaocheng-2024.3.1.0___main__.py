from http.server import    SimpleHTTPRequestHandler,    HTTPServer
Q=True
y=len
n=int
J=print
from socketserver import ThreadingMixIn
import sys
X=sys.argv
from os import path
import os
A=os.chdir

class j(ThreadingMixIn, HTTPServer):
    x = Q

def N():
    A(path.dirname(__file__))
    l = X[int("".join([chr(49)]))           ] if y(X) >int("".join([chr(49)]))                         elseint("".join([chr(51),chr(48),chr(48),chr(48)]))
    b = (("".join([chr(108),chr(111),chr(99),chr(97),chr(108),chr(104),chr(111),chr(115),chr(116)]))                    , n(l))
    SimpleHTTPRequestHandler.protocol_version =("".join([chr(72),chr(84),chr(84),chr(80),chr(47),chr(49),chr(46),chr(49)]))
    D = j(b, SimpleHTTPRequestHandler)
    J(f"Serving HTTP on localhost port {port} ...")
    D.serve_forever()

if __name__ ==("".join([chr(95),chr(95),chr(109),chr(97),chr(105),chr(110),chr(95),chr(95)]))                         : N()