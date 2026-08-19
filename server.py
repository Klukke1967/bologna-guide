import http.server
import socketserver
import os

PORT = 5055
DIRECTORY = "/Users/agenten/bologna-app"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

class TCPServerDual(socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    # Kill any existing process on 5055
    os.system("lsof -ti :5055 | xargs kill -9 2>/dev/null || true")
    with TCPServerDual(("0.0.0.0", PORT), Handler) as httpd:
        print(f"Serving Bologna App at http://0.0.0.0:{PORT}")
        httpd.serve_forever()
