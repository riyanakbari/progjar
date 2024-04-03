import socket

# Inisialisasi socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind socket ke alamat dan port tertentu
server_address = ('localhost', 5000)
sock.bind(server_address)

while True:
  print('Menunggu pesan dari client...')

  # Menerima pesan dari client
  data, address = sock.recvfrom(4096)
  print('Menerima pesan dari client:', data.decode())

  # Menghitung jumlah bilangan bulat dari pesan yang diterima
  numbers = list(map(int, data.decode().split(' ')))
  sum_integer = sum(numbers)

  
  # Mengirim balasan ke client berupa jumlah bilangan bulat
  message = str(sum_integer)

  sock.sendto(message.encode(), address)