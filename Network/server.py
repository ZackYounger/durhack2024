import socket
from _thread import *
from json import dumps, loads
import sys


def threaded_client(conn, collective_data, index=None):
  conn.send(str.encode("True"))
  data = loads(conn.recv(2048 * 16).decode("utf-8"))
  if index:
    data["playerID"] = index[-1]
  collective_data["player" + str(data["playerID"])] = data
  reply = ""
  while True:
    try:
      data = conn.recv(2048 * 16)
      reply = loads(data.decode("utf-8"))
      if index:
        conn.sendall(str.encode(dumps({"id": index, "data": collective_data})))
        index = None
      else:
        collective_data["player" + str(reply["playerID"])] = reply
        conn.sendall(str.encode(dumps(collective_data)))
    except:
      pass

  conn.close()

def start_server(collective_data):
  server = socket.gethostbyname(socket.gethostname())
  print(server)
  port = 8000

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
    s.bind((server, port))
    s.listen(2)
  except socket.error as e:
    str(e)

  print("Waiting for a connection, Server Started")
    
  while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    for i in collective_data:
      if not collective_data[i]:
        index = i
        break
    start_new_thread(threaded_client, (conn, collective_data, index))