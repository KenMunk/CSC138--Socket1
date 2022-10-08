from socket import *
targetServer = '127.0.0.1'
targetPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((targetServer, targetPort))
message = input('Please enter your lowercase sentence:\n')
encodedMessage = str.encode(message)
clientSocket.send(encodedMessage)
modifiedMessage = clientSocket.recv(1024)
print("From Server: \n" + modifiedMessage.decode())
clientSocket.close()