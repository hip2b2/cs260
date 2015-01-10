#!/usr/bin/python
# CS 260 Programming Examples
# wyu@ateneo.edu

import SocketServer
import socket
import time

class MyEchoHandler(SocketServer.BaseRequestHandler):
  def handle(self):
    print('Got connection from', self.client_address)
    self.request.sendall("thank you for connecting.")
    time.sleep(5)

HOST, PORT = "0.0.0.0", 12345
server = SocketServer.TCPServer((HOST, PORT), MyEchoHandler)
server.serve_forever()
