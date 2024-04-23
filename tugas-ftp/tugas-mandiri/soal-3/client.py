import socket

# Alamat dan IP Server
server_address = ('localhost', 12345)

# Membuat TCP Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Membuat koneksi ke server
client_socket.connect(server_address)

while True:
  # Menerima input user
  message = input("Masukkan pesan : ")

  # Mengirim pesan ke server
  client_socket.sendall(message.encode())

  # Menerima pesan respon dari server
  response = client_socket.recv(1024).decode()

  # Mencetak pesan respon
  print("Server respon:", response)

# Menutup socket
client_socket.close()