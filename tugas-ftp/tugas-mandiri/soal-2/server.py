import socket

# Inisialisasi socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind server socket ke alamat dan port tertentu
server_address = ('localhost', 12345)
server_socket.bind(server_address)

print('Server berjalan. Menunggu pesan dari client...')

while True:
  # Menerima pesan dari client
  data, client_address = server_socket.recvfrom(1024)
  
  # Menampilkan pesan yang diterima
  print(f'Pesan dari client {client_address}: {data.decode()}')
  
  # Mengirim balasan ke client
  response = 'Pesan diterima oleh server'
  server_socket.sendto(response.encode(), client_address)