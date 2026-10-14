import http.server
import socketserver

# Define the port to listen on
PORT = 8000

# Create a handler to serve files from the current directory
Handler = http.server.SimpleHTTPRequestHandler

print(f"Starting server at http://localhost:{PORT}")

# Initialize and start the TCP server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
