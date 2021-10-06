import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((192...., 4444))
client.connect(('192.....', 4444))

while True:
  client.send(input().encode("utf-8))
