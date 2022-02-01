import socket

HOST = 'localhost'
PORT = 8000
SocketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SocketObj.bind((HOST, PORT))
SocketObj.listen(5)

while True:
    connection, address = SocketObj.accept()
    print("Server connected by", address)

    while True:
        data = connection.recv(1024)
        if not data:
            break
        connection.send(b"Echo=> " + data)
    connection.close()
