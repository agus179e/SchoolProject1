from http.server import BaseHTTPRequestHandler,HTTPServer


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write("hello !")
    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write("hello !")


serv = HTTPServer(("",8080),HttpProcessor)
serv.serve_forever()
