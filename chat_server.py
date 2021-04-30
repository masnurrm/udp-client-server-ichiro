import socket

listenerSocket = socket.socket()
serverIP = "0.0.0.0"
serverPort = 2222

listenerSocket.bind((serverIP, serverPort))
listenerSocket.listen(0)
print("Siap menerima pesan")

while True:
    handlerSocket, addr = listenerSocket.accept()
    print("sebuah client terkoneksi dengan alamat: ", addr)
    while True:
        message = input("Ketikkan balasan Anda: ")
        handlerSocket.send(message[0])
        message = handlerSocket.recv(1024)
        print ("Pesan dari client: ", message)
        pass
    pass
