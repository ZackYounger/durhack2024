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
  "player3" : {}
}



def init_server():
  start_new_thread(start_server, (collective_data, ))

def game_server():
  server = socket.gethostbyname(socket.gethostname())
  port = 8000

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
    s.bind((server, port))
    s.listen(2)
  except socket.error as e:
    str(e)

  while True:
    conn, addr = s.accept()

    start_new_thread(game_server, (conn, collective_data))