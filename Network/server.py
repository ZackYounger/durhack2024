import socket
from _thread import *
from json import dumps, loads
import sys


def threaded_client(conn):
  conn.send(str.encode(dumps("test_dump")))
  reply = ""
  while True:
    try:
      data = conn.recv(2048 * 16)
      reply = loads(data.decode("utf-8"))
      conn.sendall(str.encode(dumps(reply)))
    except:
        break

  conn.close()

def start_server():
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