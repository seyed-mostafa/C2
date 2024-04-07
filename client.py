from socket import *
import time
duration = 0.05

message = "salam"

server_name = '127.0.0.1'
server_port = 12_000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

message = ''.join(format(ord(i), '08b') for i in message)

for character in message:
    if character == '1':
        time.sleep(duration * 2)
    else:
        time.sleep(duration)
    client_socket.sendall(b'@')