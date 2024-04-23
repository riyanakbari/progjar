import socket
import threading

def handle_client(client_socket):
  # Menghandle logika client
  # Fungsi ini akan dijalankan pada thread terpisah untuk setiap klien

  # Contoh
  while True:
    data = client_socket.recv(1024)
    if not data:
      break
    client_socket.send(data)

  client_socket.close()

def start_server():
  # Membuat socket TCP
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Ikat socket ke alamat dan port tertentu
  server_address = ('localhost', 12345)
  server_socket.bind(server_address)

  # Menunggu koneksi masuk
  server_socket.listen(5)
  print('Server menunggu koneksi {}:{}'.format(*server_address))

  while True:
    # Menerima koneksi dari client
    client_socket, client_address = server_socket.accept()
    print('Koneksi baru dari {}:{}'.format(*client_address))

    # Jalankan thread baru untuk menghandle client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

start_server()