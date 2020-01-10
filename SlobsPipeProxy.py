from http.server import HTTPServer, BaseHTTPRequestHandler
import socket

def postToPipe(request):
    try:
        f = open(r'\\.\pipe\slobs', 'r+b', 0)
        f.write(request)   
        f.seek(0)                         
        response = f.readline()                
        f.seek(0)
        f.close()
        return response
    except FileNotFound:    
        return -1

def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        do_POST(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        
        response = postToPipe(body)
        if(response == -1):
            self.send_error(404,"SLOBS does not seem to be running")
            self.end_headers()
            self.wfile.write(bytes("SLOBS does not seem to be running", 'utf8'))
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(response)

try:
    ip = getIP()
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    print(f"Started SLOBS server on port 8000 at {ip}")
	
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the SLOBS server')
    server.socket.close()
