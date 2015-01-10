#!/usr/bin/python
# CS 260 Programming Examples
# wyu@ateneo.edu

import SocketServer
import threading
import time

class ThreadingTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer): 
  pass

class MyEchoHandler(SocketServer.BaseRequestHandler):
  def handle(self):
    print('Got connection from', self.client_address)
    self.request.sendall("thank you for connecting.")
    time.sleep(5)

HOST, PORT = "0.0.0.0", 12345
server = ThreadingTCPServer((HOST, PORT), MyEchoHandler)
server_thread = threading.Thread(target=server.serve_forever)
server_thread.start()
