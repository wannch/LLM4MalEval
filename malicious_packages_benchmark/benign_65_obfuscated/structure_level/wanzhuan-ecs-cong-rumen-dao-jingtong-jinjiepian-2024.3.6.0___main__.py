from socketserver import ThreadingMixIn
from http.server import SimpleHTTPRequestHandler, HTTPServer
from os import path
if False:
    _var_164_0 = (878, 59, 156)
    _var_164_1 = (679, 743, 188)

    def _var_164_fn():
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
    if False:
        _var_162_0 = (39, 29, 1000)

        def _var_162_fn():
            pass
    svr.serve_forever()
    if False:
        _var_163_0 = (677, 737, 168)
        _var_163_1 = (14, 749, 174)
        _var_163_2 = (608, 921, 419)

        def _var_163_fn():
            pass
if __name__ == '__main__':
    main()