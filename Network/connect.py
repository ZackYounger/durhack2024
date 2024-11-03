import network
from network import Network
from server import start_server
from time import sleep
from _thread import *

collective_data = {
  "player0" : {},
  "player1" : {},
  "player2" : {},
  "player3" : {}
}


host = "169.254.131.250"

def start_server():
  start_new_thread(start_server, (collective_data))

def waiting_screen():
  for i in collective_data:
    if not collective_data[i]:
      return 4 - int(i[-1])