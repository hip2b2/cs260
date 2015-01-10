#!/usr/bin/python
# CS 260 Programming Examples
# wyu@ateneo.edu

import SocketServer
import socket

class MyEchoHandler(SocketServer.BaseRequestHandler):

  def handle(self):
    self.data = self.request.recv(1024).strip()
    print "{} wrote:".format(self.client_address[0])
    print self.data
    self.request.sendall(self.data.upper())

#if __name__ == "__main__":
HOST, PORT = socket.gethostname(), 12345
server = SocketServer.TCPServer((HOST, PORT), MyEchoHandler)
server.serve_forever()
