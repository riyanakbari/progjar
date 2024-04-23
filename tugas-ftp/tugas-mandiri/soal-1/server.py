import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

msgFromServer = "Halo UDP Client"
bytesToSend = str.encode(msgFromServer)

# Membuat datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Melakukan bind ke alamat dan IP
UDPServerSocket.bind((localIP, localPort))
print("Server UDP aktif dan siap menerima data")

# Mendengarkan datagram yang masuk
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Pesan dari Client :{}".format(message)
    clientIP = "Alamat IP Client :{}".format(address)

    print(clientMsg)
    print(clientIP)

    # Mengirim pesan balasan ke client
    UDPServerSocket.sendto(bytesToSend, address)