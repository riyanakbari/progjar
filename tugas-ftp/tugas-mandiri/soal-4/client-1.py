import socket

# Alamat dan IP Server
server_address = 'localhost'
server_port = 12345

# Membuat TCP Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Membuat koneksi ke server
client_socket.connect((server_address, server_port))

# Mengirim data ke server
data = 'Halo, server! saya client 1'
client_socket.send(data.encode())

# Menerima respon dari server
response = client_socket.recv(1024).decode()
print('Respon dari server :', response)

# Menutup koneksi
client_socket.close()