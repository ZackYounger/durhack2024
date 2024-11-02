import socket
from json import loads, dumps
from time import time




class Network:
  def __init__(self, ip):
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server = ip
    self.port = 8000
    self.addr = (self.server, self.port)
    self.connected = self.connect()

  def connect(self):
    try:
      self.client.connect(self.addr)
      connect_msg = self.client.recv(2048 * 16).decode()
      if connect_msg == "True":
        return True
      else:
        raise Exception("No Connection")
        return False
    except socket.error as e:
      print(e)
      


  def ping(self, data):
    try:
      if self.connected:
        self.client.send(str.encode(dumps(data)))
        return loads(self.client.recv(2048 * 16).decode())
      else:
        raise Exception("No Connection")
    except socket.error as e:
      print(e)
  
