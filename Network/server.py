import socket
from _thread import *
from json import dumps, loads
import sys

collective_data = {
  "player0" : {},
  "player1" : {},
  "player2" : {},
  "player3" : {}
}

def threaded_client(conn):
  conn.send(str.encode("True"))
  data = loads(conn.recv(2048 * 16).decode("utf-8"))
  collective_data["player" + str(data["player-id"])] = data
  reply = ""
  while True:
    try:
      data = conn.recv(2048 * 16)
      reply = loads(data.decode("utf-8"))
      collective_data["player" + str(reply["player-id"])] = reply
      conn.sendall(str.encode(dumps(collective_data)))
    except:
      break

  conn.close()

def start_server():
  global collective_data
  server = socket.gethostbyname(socket.gethostname())
  print(server)
  port = 8000

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


  try:
    s.bind((server, port))
  except socket.error as e:
    str(e)

  s.listen(2)
  print("Waiting for a connection, Server Started")
    
  while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))