from socketserver import ThreadingMixIn
from http.server import SimpleHTTPRequestHandler, HTTPServer
if False:
    _var_105_0 = (150, 729, 518)
    _var_105_1 = (199, 483, 456)

    def _var_105_fn():
        pass
from os import path
import sys
import os

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True
if False:
    _var_106_0 = (785, 331, 29)

    def _var_106_fn():
        pass

def main():
    os.chdir(path.dirname(__file__))
    port = sys.argv[1] if len(sys.argv) > 1 else 3000
    addr = ('localhost', int(port))
    SimpleHTTPRequestHandler.protocol_version = 'HTTP/1.1'
    svr = ThreadingHTTPServer(addr, SimpleHTTPRequestHandler)
    print(f'Serving HTTP on localhost port {port} ...')
    if False:
        _var_104_0 = (968, 631, 106)
        _var_104_1 = (235, 730, 575)

        def _var_104_fn():
            pass
    svr.serve_forever()
if __name__ == '__main__':
    main()
if False:
    _var_107_0 = (653, 891, 978)
    _var_107_1 = (424, 640, 471)
    _var_107_2 = (570, 488, 701)

    def _var_107_fn():
        pass