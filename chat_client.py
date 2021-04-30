import socket

handlerSocket = socket.socket()
serverIP = "127.0.0.1"
serverPort = 2222

handlerSocket.connect((serverIP, serverPort))
print('Connected to server')
# clientName = input("Masukkan nama Anda: ")

while True:
    message = handlerSocket.recv(1024)
    print("pesan dari server: ", message)
    message = input('Ketikkan balasan Anda: ')
    handlerSocket.send(message)
    pass
