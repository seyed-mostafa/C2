from socket import *
import time
duration = 0.05


server_port = 12_000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("", server_port))
server_socket.listen(1)
print("server ready to receive")

connection_socket, addr = server_socket.accept()
print("new connection was accepted")

message = ""
start_transfer = time.time()

while True:
    start = time.time()
    data = connection_socket.recv(1)
    finish = time.time()

    if not data:
        break
    if finish - start >= duration * 2:
        message += '1'
    else:
        message += '0'
finish_transfer = time.time()
time = finish_transfer - start_transfer
speed = len(message) / time


print("binary message: ", message)
final_message = ""
for i in range(0, len(message), 8):
    character = chr(int(message[i:i + 8], 2))
    print(character)
    final_message += character

print("string message: ", final_message)
print("transfer speed is: ", speed, "bit/s")
