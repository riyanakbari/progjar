import socket

# Alamat IP dan Port Server
server_ip = '127.0.0.1'
server_port = 12345

# Membuat UDP Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Mengirim pesan secara terus menerus
while True:
  message = input("Masukkan pesan : ")

  # Mengirim pesan ke server
  client_socket.sendto(message.encode(), (server_ip, server_port))

  # Menerima pesan respon dari server
  response, server_address = client_socket.recvfrom(1024)
  print("Respon dari server :", response.decode())

# Menutup Socket
client_socket.close()