from socket import *
udpPort = 12001
udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.bind(('',udpPort))
print('The server is probably ready to receive')
while 1:
    message, clientAddress = udpSocket.recvfrom(2048)
    print("Received: " + str(message))
    modifiedMessage = str.encode(message.decode().upper())
    print("Sending: " + str(modifiedMessage))
    udpSocket.sendto(modifiedMessage, clientAddress)