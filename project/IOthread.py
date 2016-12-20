import threading
import socket
import time
class ITHR(threading.Thread):
    def __init__(self,port,f,l,e,e1):
        threading.Thread.__init__(self)
        self.sock=socket.socket()
        self.sock.bind(('',port))
        self.f=f
        self.l=l
        self.e=e
        self.e1=e1
        self.e1.set()
    def run(self):
        while True:
            try:
                self.sock.listen(10)
                conn, addr=self.sock.accept()
                while True:
                    data=conn.recv(2048)
                    udata=data.decode('utf-8')
                    self.e1.wait()
                    self.e1.clear()
                    self.f[0]=udata
                    self.e.set()
            finally:
                print('error')
class OTHR(threading.Thread):
    def __init__(self,addr,f,l,e,e1):
        threading.Thread.__init__(self)
        self.sock=socket.socket()
        self.addr=addr
        self.f=f
        self.l=l
        self.e=e
        self.e1=e1
        self.e1.set()
    def run(self):
        while True:
            try:
                self.sock.connect(self.addr)
                while True:
                    self.e1.wait()
                    self.e1.clear()
                    self.l.acquire()
                    udata=self.f[0]
                    data=bytearray(udata,'utf-8')
                    self.l.release()
                    self.sock.send(data)
                    e.set()
            finally:
                print('error')

class reader(threading.Thread):
    def __init__(self,f,e,e1,l):
        threading.Thread.__init__(self)
        self.f=f
        self.e=e
        self.e1=e1
        self.l=l
    def run(self):
        while True:
            self.e.wait()
            self.e.clear()
            print(self.f[0])
            self.e1.set()
class writer(threading.Thread):
    def __init__(self,f,e,e1,l):
        threading.Thread.__init__(self)
        self.f=f
        self.e=e
        self.e1=e1
        self.l=l
    def run(self):
        while True:
            self.e.wait()
            self.e.clear()
            self.f[0]=input()
            self.e1.set()
l=threading.Lock()   
e=threading.Event()
e1=threading.Event()
f=['1']
if __name__ == '__main__':
    if input() == 'out':
        x=OTHR(('localhost',8080),f,l,e,e1)
        y=writer(f,e,e1,l)
        x.start()
        y.start()
        x.join()
        y.join()
    else:
        x=ITHR(8080,f,l,e,e1)
        y=reader(f,e,e1,l)
        x.start()
        y.start()
        x.join()
        y.join()
    
        

    
        
            
            
            
    
