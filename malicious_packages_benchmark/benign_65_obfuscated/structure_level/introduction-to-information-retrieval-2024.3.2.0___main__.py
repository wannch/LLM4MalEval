from socketserver import ThreadingMixIn
from http.server import SimpleHTTPRequestHandler, HTTPServer
from os import path
import sys
if False:
    _var_137_0 = (376, 230, 414)
    _var_137_1 = (55, 894, 983)
    _var_137_2 = (614, 503, 108)

    def _var_137_fn():
        pass
import os
if False:
    _var_138_0 = (82, 843, 14)

    def _var_138_fn():
        pass

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

def main():
    os.chdir(path.dirname(__file__))
    port = sys.argv[1] if len(sys.argv) > 1 else 3000
    addr = ('localhost', int(port))
    SimpleHTTPRequestHandler.protocol_version = 'HTTP/1.1'
    svr = ThreadingHTTPServer(addr, SimpleHTTPRequestHandler)
    if False:
        _var_136_0 = (801, 227, 531)

        def _var_136_fn():
            pass
    print(f'Serving HTTP on localhost port {port} ...')
    svr.serve_forever()
if False:
    _var_139_0 = (709, 637, 320)
    _var_139_1 = (917, 666, 97)
    _var_139_2 = (733, 401, 750)

    def _var_139_fn():
        pass
if __name__ == '__main__':
    main()