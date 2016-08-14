import time
import BaseHTTPServer
import cgi
import json

HOST_NAME = ''
PORT_NUMBER = 9000


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
    def do_GET(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(self.get_next_page())
        
    def do_POST(self):
        """Respond to a POST request."""
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        data = json.loads(post_body)
        print data['payload']['title']
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(self.get_next_page())


    def push_to_database(self, payload):
        """Push the payload received from Chrome to the database"""
        pass


    def get_next_page(self):
        """Return the next page to be scraped to Chrome"""
        return json.dumps({"nextpage": "http://www.randomwebsite.com/cgi-bin/random.pl"})

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print "Server running at - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
