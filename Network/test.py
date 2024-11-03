import network
from network import Network
from server import start_server
from time import sleep
from _thread import *

host = "192.168.122.1"

start_new_thread(start_server, ({}, ))

first = Network(host, {"player-id": 0, "x": 10, "y": 5})
second = Network(host, {"player-id": 1, "x": 25, "y": 5})
third = Network(host, {"player-id": 2, "x": 10, "y": 15})
fourth = Network(host, {"player-id": 3, "x": 25, "y": 15})

while True:
  print(first.ping({"player-id": 0, "x": 10, "y": 5}))
  sleep(1.5)
  print(second.ping({"player-id": 1, "x": 10, "y": 5}))
  sleep(1.5)
  print(second.ping({"player-id": 1, "x": 10, "y": 5}))
