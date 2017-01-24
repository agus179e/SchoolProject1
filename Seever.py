from http.server import BaseHTTPRequestHandler,HTTPServer
import threading, os, time


class HttpThread(threading.Thread):
    
    def __init__(self,l,e1,e2,num):
        self.num=num
        self.f="<META HTTP-EQUIV=REFRESH CONTENT=0.5><iframe src=http://localhost:8089/strelka"+num[0]+".html width=500 height=500 frameborder=no scrolling=no></iframe>"
        threading.Thread.__init__(self)
        self.HttpProcessor.f=self.f
        
        
        

    class HttpProcessor(BaseHTTPRequestHandler):
        f=""
        def do_GET(self):
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.send_header('Access-Control-Allow-Origin','http://localhost:8089')
            self.end_headers()
            self.wfile.write(bytearray(self.f,"utf-8"))

    def run(self):
        

        serv = HTTPServer(("",8080),self.HttpProcessor)
        serv.serve_forever()
os.system("start.bat")
num=["0"]
l=threading.Lock()
e1=threading.Event()
e2=threading.Event()
httpm=HttpThread(l,e1,e2,num)

httpm.start()
time.sleep(10)
HttpThread.HttpProcessor.f="<META HTTP-EQUIV=REFRESH CONTENT=0.5><iframe src=http://localhost:8089/strelka45.html width=500 height=500 frameborder=no scrolling=no></iframe>"
httpm.join()
