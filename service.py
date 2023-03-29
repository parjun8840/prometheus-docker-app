import http.server
import time
import socket
from prometheus_client import start_http_server, Histogram, Counter

REQUEST_RESPOND_TIME = Histogram('app_response_latency_seconds', 'Response latency in seconds', buckets=[0.1,0.5,1,2,3,4,5,10])
REQUEST_COUNT = Counter('app_requests_count', 'total app http request count', labelnames=['server_type','endpoint'])
APP_PORT = 8000
METRICS_PORT = 8001

class HandleRequests(http.server.BaseHTTPRequestHandler):

    @REQUEST_RESPOND_TIME.time()
    def do_GET(self):
        REQUEST_COUNT.labels('parjun8840-frontend',self.path).inc()
        #start_time = time.time()
        time.sleep(1)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Author", "ArjunPandey")
        self.end_headers()
        host_name = socket.gethostname()
        self.wfile.write(bytes("<html><head><title>Business Transaction Application</title></head>", "utf-8"))
        self.wfile.write(bytes("<body style='color: #333; margin-top: 30px;'><center><h2>Every time you refresh the page you get 100$.</center></h2>", "utf-8"))
        self.wfile.write(bytes("<p><center>You accessed path: %s</p></center>" % self.path,  "utf-8"))
        self.wfile.write(bytes("<p><center>Your IP: %s</p></center>" %self.client_address[0],  "utf-8"))
        self.wfile.write(bytes("<p><center>Remote HostName: %s</p></center>" %host_name,"utf-8"))
        self.wfile.write(bytes("</body></html>",  "utf-8"))
        #time_taken = time.time() - start_time
        #REQUEST_RESPOND_TIME.observe(time_taken)


if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    server = http.server.HTTPServer(('0.0.0.0', APP_PORT), HandleRequests)
    server.serve_forever()
