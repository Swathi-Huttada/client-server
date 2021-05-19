import socket
client_socket = socket.socket()
port = 1234
client_socket.connect(('127.0.0.1',port))
msg = input("-> ")
while True:

    if msg == 'exit':
        break;
    else:
        client_socket.send(msg.encode())
    msg = input("-> ")

client_socket.close()
