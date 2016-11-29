# encoding: utf-8

import json
import os
from tagger import Tagger
try:
    from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
    from SocketServer import TCPServer as Server
except ImportError:
    from http.server import SimpleHTTPRequestHandler as Handler
    from http.server import HTTPServer as Server


class ServerHandler(Handler):

    def _set_headers(self, content_type="text/html"):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        tagger = Tagger()
        response = tagger.run(post_data)

        print "Posting results"
        self._set_headers("application/json")
        self.wfile.write(json.dumps(response))

    def do_GET(self):
      self._set_headers()
      self.wfile.write("Playing with NLTK")

# Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8000))
os.chdir('.')

httpd = Server(("", PORT), ServerHandler)
try:
    print("Start serving at port %i" % PORT)
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
