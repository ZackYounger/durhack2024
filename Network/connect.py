import socket
import Network.network
from Network.network import Network
from Network.server import start_server
from time import sleep
from _thread import *

collective_data = {
  "player0" : {},
  "player1" : {},
  "player2" : {},
  "player3" : {},
  "game_state": "",
}



def init_server():
  start_new_thread(start_server, (collective_data, ))
