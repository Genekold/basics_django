from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostname = "localhost"
serverport = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open('contacts.html', 'r', encoding='utf-8') as file:
            data = file.read()
            self.wfile.write(bytes(data, 'utf-8'))


if __name__ == "__main__":

    webserver = HTTPServer((hostname, serverport), MyServer)
    print("Server started http://%s:%s" % (hostname, serverport))

    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass

    webserver.server_close()
    print("Server stopped.")
