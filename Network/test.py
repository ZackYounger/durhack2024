import network
from network import Network
from server import start_server
from time import sleep
from _thread import *

host = "169.254.131.250"

start_new_thread(start_server, ())

first = Network(host)
second = Network(host)

while True:
  print(first.ping("ping1"))
  sleep(1.5)
  print(second.ping("2_ping"))
  sleep(1.5)
  print(second.ping("3_ping"))
