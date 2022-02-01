import sys
import socket

serverHost = 'localhost'
serverPort = 50981

message = [b"We are in the net !"]

if len(sys.argv) > 1:
    serverHost = sys.argv[1]
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:])

socketObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketObj.connect((serverHost, serverPort))

for line in message:
    socketObj.send(line)
    data = socketObj.recv(1024)
    print("Client received: ", data)

socketObj.close()
