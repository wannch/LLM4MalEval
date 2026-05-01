from socketserver import ThreadingMixIn
from http.server import SimpleHTTPRequestHandler, HTTPServer
from os import path
if False:
    _var_21_0 = (548, 386, 129)

    def _var_21_fn():
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
    if False:
        _var_18_0 = (838, 375, 941)
        _var_18_1 = (166, 433, 947)

        def _var_18_fn():
            pass
    svr = ThreadingHTTPServer(addr, SimpleHTTPRequestHandler)
    if False:
        _var_19_0 = (238, 228, 888)

        def _var_19_fn():
            pass
    print(f'Serving HTTP on localhost port {port} ...')
    if False:
        _var_20_0 = (431, 344, 931)
        _var_20_1 = (605, 201, 415)

        def _var_20_fn():
            pass
    svr.serve_forever()
if __name__ == '__main__':
    main()