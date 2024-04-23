import socket

msgFromClient = input("Masukkan pesan : ")  # User Input
bytesToSend = str.encode(msgFromClient)

serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

# Membuat Socket UDP pada sisi client
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Mengirim ke server menggunakan UDP Socket yang telah dibuat
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Pesan dari Server {}".format(msgFromServer[0])
print(msg)