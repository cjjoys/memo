D:\bin\util>type readme.txt

  D:\bin\util>python http_server.py 8080
  D:\bin\util>python tcp_server.py 9000

===

D:\bin\util>type http_server.py
from http.server import HTTPServer, BaseHTTPRequestHandler
import sys

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'HTTP GET success')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python " + sys.argv[0] + " <port>")
        sys.exit(1)

    port = int(sys.argv[1])
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Server running on http://127.0.0.1:{port}")
    httpd.serve_forever()


D:\bin\util>type tcp_server.py
import socket
import sys
import signal

def signal_handler(sig, frame):
    print("\nProgram terminated by user")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if len(sys.argv) != 2:
    print("Usage: python  " + sys.argv[0] + "  <port>")
    sys.exit(1)

port = int(sys.argv[1])
host = '127.0.0.1'  # localhost

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print(f"Server listening on {host}:{port}")

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            conn.sendall(b"TCP Connection success")

            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode('utf-8')}")
D:\bin\util>























































































































































































































































































































































































