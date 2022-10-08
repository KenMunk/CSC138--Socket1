from socket import *
tcpPort = 12001
tcpSocket = socket(AF_INET, SOCK_STREAM)
tcpSocket.bind(('',tcpPort))
tcpSocket.listen(1)
print('The server is probably ready to receive')
while 1:
    tcpConnection, tcpAddr = tcpSocket.accept()
    
    message = tcpConnection.recv(1024)
    print("Received: " + str(message))
    modifiedMessage = str.encode(message.decode().upper())
    print("Sending: " + str(modifiedMessage))
    tcpConnection.send(modifiedMessage)
    tcpConnection.close()