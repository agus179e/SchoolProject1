from IOthread import *
import socket
sk=socket.socket()
try:
    sk.connect(('localhost',8080))
    sk.settimeout(5)
    vv=sk.recv(2048)
    import iprg
except socket.timeout:
    import oprg
except ConnectionRefusedError:
    import oprg
