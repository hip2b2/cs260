#!/usr/bin/python
# CS 260 Programming Examples
# wyu@ateneo.edu

import socket
import thread
import time

def connection_handler (threadName, socket, addr):
  print('Got connection from', addr)
  c.send('Thank you for connecting')
  time.sleep(5)
  c.close()

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)

while True:
  c, addr = s.accept()
  thread.start_new_thread( connection_handler, ("ThreadedServer", c, addr) )

