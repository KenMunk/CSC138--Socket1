from socket import *
targetServer = '127.0.0.1'
targetPort = 12001
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Please enter your lowercase sentence:\n')
encodedMessage = str.encode(message)
clientSocket.sendto(encodedMessage, (targetServer, targetPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()