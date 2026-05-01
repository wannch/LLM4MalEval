from socketserver import ThreadingMixIn
from http.server import SimpleHTTPRequestHandler, HTTPServer
if False:
    _var_1_0 = (839, 896, 238)

    def _var_1_fn():
        pass
from os import path
import sys
import os

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True
if False:
    _var_2_0 = (962, 648, 984)

    def _var_2_fn():
        pass

def main():
    os.chdir(path.dirname(__file__))
    port = sys.argv[1] if len(sys.argv) > 1 else 3000
    addr = ('localhost', int(port))
    SimpleHTTPRequestHandler.protocol_version = 'HTTP/1.1'
    svr = ThreadingHTTPServer(addr, SimpleHTTPRequestHandler)
    print(f'Serving HTTP on localhost port {port} ...')
    svr.serve_forever()
if __name__ == '__main__':
    main()