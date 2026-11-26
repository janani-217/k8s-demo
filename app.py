from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import socket

PORT = int(os.getenv("PORT", "8080"))
APP_VERSION = os.getenv("APP_VERSION", "v1")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = (
            f"Hello from {APP_VERSION}!\n"
            f"Pod / Container Hostname: {socket.gethostname()}\n"
            f"Path requested: {self.path}\n"
        ).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        print(f"[{APP_VERSION}] {self.address_string()} - {format % args}")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Python server ({APP_VERSION}) listening on port {PORT}", flush=True)
    server.serve_forever()
