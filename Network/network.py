import configparser
import socket
from json import loads
from time import time



class Network:
  def __init__(self, ip):
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server = ip
    self.port = 8000
    self.addr = (self.server, self.port)
    self.id = self.connect()

  def connect(self):
    try:
      self.client.connect(self.addr)
      return loads(self.client.recv(512).decode())
    except:
      pass
      
  def ping(self, data):
    try:
      self.client.send(str.encode(data))
      return self.client.recv(512).decode()
    except socket.error as e:
      print(e)

n = Network("10.247.180.48")
lastping = time()
while True:
  print(n.ping(str(time() - lastping)))
  lastping = time()