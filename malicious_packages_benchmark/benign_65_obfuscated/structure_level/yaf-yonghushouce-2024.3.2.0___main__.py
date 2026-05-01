from socketserver import ThreadingMixIn
from http.server import SimpleHTTPRequestHandler, HTTPServer
from os import path
import sys
import os

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True
if False:
    _var_121_0 = (612, 990, 627)
    _var_121_1 = (745, 318, 193)

    def _var_121_fn():
        pass

def main():
    os.chdir(path.dirname(__file__))
    port = sys.argv[1] if len(sys.argv) > 1 else 3000
    addr = ('localhost', int(port))
    SimpleHTTPRequestHandler.protocol_version = 'HTTP/1.1'
    svr = ThreadingHTTPServer(addr, SimpleHTTPRequestHandler)
    if False:
        _var_118_0 = (413, 1, 869)
        _var_118_1 = (705, 380, 838)
        _var_118_2 = (817, 853, 806)

        def _var_118_fn():
            pass
    print(f'Serving HTTP on localhost port {port} ...')
    if False:
        _var_119_0 = (894, 182, 944)
        _var_119_1 = (996, 390, 353)

        def _var_119_fn():
            pass
    svr.serve_forever()
    if False:
        _var_120_0 = (178, 194, 526)
        _var_120_1 = (704, 300, 587)
        _var_120_2 = (608, 926, 644)

        def _var_120_fn():
            pass
if __name__ == '__main__':
    main()
if False:
    _var_122_0 = (929, 979, 467)
    _var_122_1 = (162, 232, 28)
    _var_122_2 = (589, 459, 381)

    def _var_122_fn():
        pass