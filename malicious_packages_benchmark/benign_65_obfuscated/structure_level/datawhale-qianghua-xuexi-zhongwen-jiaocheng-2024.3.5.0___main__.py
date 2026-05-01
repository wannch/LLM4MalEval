from socketserver import ThreadingMixIn
if False:
    _var_33_0 = (52, 168, 31)
    _var_33_1 = (488, 705, 180)

    def _var_33_fn():
        pass
from http.server import SimpleHTTPRequestHandler, HTTPServer
from os import path
import sys
import os

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

def main():
    os.chdir(path.dirname(__file__))
    port = sys.argv[1] if len(sys.argv) > 1 else 3000
    addr = ('localhost', int(port))
    if False:
        _var_32_0 = (149, 204, 280)
        _var_32_1 = (712, 150, 225)

        def _var_32_fn():
            pass
    SimpleHTTPRequestHandler.protocol_version = 'HTTP/1.1'
    svr = ThreadingHTTPServer(addr, SimpleHTTPRequestHandler)
    print(f'Serving HTTP on localhost port {port} ...')
    svr.serve_forever()
if False:
    _var_34_0 = (332, 766, 120)

    def _var_34_fn():
        pass
if __name__ == '__main__':
    main()