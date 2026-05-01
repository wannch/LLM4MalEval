from socketserver import ThreadingMixIn
from http.server import SimpleHTTPRequestHandler, HTTPServer
from os import path
import sys
import os

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

def main():
    os.chdir(path.dirname(__file__))
    if False:
        _var_168_0 = (964, 106, 112)
        _var_168_1 = (792, 519, 70)

        def _var_168_fn():
            pass
    port = sys.argv[1] if len(sys.argv) > 1 else 3000
    addr = ('localhost', int(port))
    SimpleHTTPRequestHandler.protocol_version = 'HTTP/1.1'
    svr = ThreadingHTTPServer(addr, SimpleHTTPRequestHandler)
    if False:
        _var_169_0 = (207, 209, 185)
        _var_169_1 = (7, 721, 504)

        def _var_169_fn():
            pass
    print(f'Serving HTTP on localhost port {port} ...')
    svr.serve_forever()
if __name__ == '__main__':
    main()