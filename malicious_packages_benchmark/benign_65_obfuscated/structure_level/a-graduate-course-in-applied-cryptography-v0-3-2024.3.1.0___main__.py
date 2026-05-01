from socketserver import ThreadingMixIn
from http.server import SimpleHTTPRequestHandler, HTTPServer
from os import path
if False:
    _var_51_0 = (262, 393, 488)

    def _var_51_fn():
        pass
import sys
if False:
    _var_52_0 = (676, 920, 267)

    def _var_52_fn():
        pass
import os
if False:
    _var_53_0 = (956, 971, 676)

    def _var_53_fn():
        pass

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

def main():
    os.chdir(path.dirname(__file__))
    port = sys.argv[1] if len(sys.argv) > 1 else 3000
    addr = ('localhost', int(port))
    SimpleHTTPRequestHandler.protocol_version = 'HTTP/1.1'
    if False:
        _var_50_0 = (323, 413, 862)
        _var_50_1 = (514, 759, 82)
        _var_50_2 = (33, 353, 123)

        def _var_50_fn():
            pass
    svr = ThreadingHTTPServer(addr, SimpleHTTPRequestHandler)
    print(f'Serving HTTP on localhost port {port} ...')
    svr.serve_forever()
if __name__ == '__main__':
    main()
if False:
    _var_54_0 = (143, 338, 754)
    _var_54_1 = (179, 284, 389)

    def _var_54_fn():
        pass