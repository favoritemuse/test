from http.server import BaseHTTPRequestHandler, HTTPServer
import base64
import time
import psutil

host_name = '0.0.0.0'
host_port = 80

key = base64.b64encode(
            bytes('{}:{}'.format('test', 'test'), 'utf-8')
).decode('ascii')


class MyServer(BaseHTTPRequestHandler):
    def do_HEAD(self):
        memory = psutil.virtual_memory()
        cpu = psutil.cpu_percent()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Computer stats.</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>CPU usage percent: {}</p>".format(cpu), "utf-8"))
        self.wfile.write(bytes("<p>Memory usage percent: {}</p>".format(memory.percent), "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_GET(self):
        if not self.headers.get('Authorization'):
            self.do_AUTHHEAD()
            self.wfile.write(bytes('no auth header received', 'utf-8'))
            pass
        elif self.headers.get('Authorization') == 'Basic {}'.format(key):
            self.do_HEAD()
            pass
        else:
            self.do_AUTHHEAD()
            self.wfile.write(bytes(self.headers.get('Authorization'), 'utf-8'))
            self.wfile.write(bytes('Not authenticated!', 'utf-8'))
            pass

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Test\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()


myServer = HTTPServer((host_name, host_port), MyServer)
print(time.asctime(), "Server Starts - {}:{}".format(host_name, host_port))

try:
    myServer.serve_forever()
except Exception as e:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - {}:{}".format(host_name, host_port))
