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

  # palindrome
  message = data.decode()
  if message == message[::-1]:
    message = 'Kata tersebut merupakan Palindrome'
  else:
    message = 'Kata tersebut bukan palindrome'

  # Mengirim balasan ke client apakah palindrome atau bukan
  sock.sendto(message.encode(), address)