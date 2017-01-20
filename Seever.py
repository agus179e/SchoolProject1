from http.server import BaseHTTPRequestHandler,HTTPServer
import threading, os
os.system("start.bat")

class httpseedthread(threading.Thread):
    
    def __init__(self,f):
        num="0"
        self.f="<iframe src=http://localhost:8089/strelka"+num+".html width=500 height=500></iframe>"
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

    def start(self):
        

        serv = HTTPServer(("",8080),self.HttpProcessor)
        serv.serve_forever()

httpm=httpseedthread(f)

httpm.start()
httpm.join()
