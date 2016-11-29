import os
from tagger import Tagger
try:
    from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
    from SocketServer import TCPServer as Server
except ImportError:
    from http.server import SimpleHTTPRequestHandler as Handler
    from http.server import HTTPServer as Server


class ServerHandler(Handler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        # <--- Gets the size of data
        content_length = int(self.headers['Content-Length'])
        # <--- Gets the data itself
        post_data = self.rfile.read(content_length)
        tagger = Tagger()
        self._set_headers()
        self.wfile.write(tagger.run(post_data))

    def do_GET(self):
      self._set_headers()
      self.wfile.write("Playing with NLTK")

# Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8000))

httpd = Server(("", PORT), ServerHandler)
try:
    print("Start serving at port %i" % PORT)
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
