from socketserver import ThreadingMixIn
from http.server import SimpleHTTPRequestHandler, HTTPServer
from os import path
if False:
    _var_31_0 = (775, 760, 767)

    def _var_31_fn():
        pass
import sys
import os

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

def main():
    os.chdir(path.dirname(__file__))
    port = sys.argv[1] if len(sys.argv) > 1 else 3000
    addr = ('localhost', int(port))
    SimpleHTTPRequestHandler.protocol_version = 'HTTP/1.1'
    svr = ThreadingHTTPServer(addr, SimpleHTTPRequestHandler)
    print(f'Serving HTTP on localhost port {port} ...')
    svr.serve_forever()
    if False:
        _var_30_0 = (967, 460, 282)
        _var_30_1 = (860, 52, 451)
        _var_30_2 = (102, 0, 395)

        def _var_30_fn():
            pass
if __name__ == '__main__':
    main()