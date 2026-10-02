from http.server import BaseHTTPRequestHandler, HTTPServer
import os


ENVIRONMENT = os.getenv("APP_ENV", "dev")


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        message = f"""
        Jenkins CI/CD Deployment
        Environment: {ENVIRONMENT}
        """

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())

    def log_message(self, format, *args):
        return


server = HTTPServer(("0.0.0.0", 5000), Handler)

print(f"Application running on port 5000")
print(f"Environment: {ENVIRONMENT}")

server.serve_forever()
