import http.server
import socketserver
import os

# ----------------------------
# Run a simple HTTP server to serve our app during tests.
# This will allow us to access our app at http://localhost:8000/index.html
# ----------------------------s
PORT = 8000
DIRECTORY = "app"

os.chdir(DIRECTORY)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
