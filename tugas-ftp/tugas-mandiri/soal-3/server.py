import socket

# Membuat TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menentukan alamat server dan portnya
server_address = ('localhost', 12345)

# Bind server socket ke alamat dan port tertentu
server_socket.bind(server_address)

# Menunggu koneksi masuk
server_socket.listen(1)

print('Server berjalan. Menunggu pesan dari client...')

while True:
  # Menunggu client untuk terhubung
  client_socket, client_address = server_socket.accept()
  print(f'Client terhubung : {client_address}')

  try:
    while True:
      # Menerima data dari client
      data = client_socket.recv(1024).decode()

      if not data:
        # Jika tidak ada data yang diterima, klien telah terputus
        print(f'Client terputus : {client_address}')
        break

      # Memproses data yang diterima
      print(f'Data yang diterima dari client {client_address}: {data}')

      # Mengirim balasan ke client
      response = 'Pesan diterima oleh server : ' + data
      client_socket.sendall(response.encode())

  finally:
    # Menutup socket client
    client_socket.close()

# Menutup socket server
server_socket.close()