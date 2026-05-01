from socketserver import ThreadingMixIn
from http.server import SimpleHTTPRequestHandler, HTTPServer
if False:
    _var_125_0 = (16, 977, 877)
    _var_125_1 = (910, 50, 218)

    def _var_125_fn():
        pass
from os import path
import sys
if False:
    _var_126_0 = (650, 234, 468)

    def _var_126_fn():
        pass
import os

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True
if False:
    _var_127_0 = (798, 554, 8)
    _var_127_1 = (258, 452, 399)
    _var_127_2 = (817, 892, 614)

    def _var_127_fn():
        pass

def main():
    os.chdir(path.dirname(__file__))
    port = sys.argv[1] if len(sys.argv) > 1 else 3000
    addr = ('localhost', int(port))
    if False:
        _var_123_0 = (241, 799, 551)
        _var_123_1 = (403, 223, 938)
        _var_123_2 = (996, 871, 15)

        def _var_123_fn():
            pass
    SimpleHTTPRequestHandler.protocol_version = 'HTTP/1.1'
    svr = ThreadingHTTPServer(addr, SimpleHTTPRequestHandler)
    print(f'Serving HTTP on localhost port {port} ...')
    if False:
        _var_124_0 = (815, 165, 267)

        def _var_124_fn():
            pass
    svr.serve_forever()
if __name__ == '__main__':
    main()
if False:
    _var_128_0 = (957, 770, 229)
    _var_128_1 = (624, 574, 772)

    def _var_128_fn():
        pass