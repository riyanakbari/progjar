# Tugas 1 - Socket Programming On Python
## Soal & Jawaban

1. Membuat sebuah program server yang dapat menerima koneksi dari klien menggunakan protokol TCP. Server ini akan menerima pesan dari klien dan mengirimkan pesan balasan berisi jumlah karakter pada pesan tersebut. Gunakan port 12345 untuk server. Membuat analisa dari hasil program tersebut 

Source Code :

```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'localhost'
PORT = 12345

server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("Waiting...")

client_socket, client_address = server_socket.accept()
data = client_socket.recv(1024)
jumlahKata = len(data.decode())

print("Request dari client :", data.decode())
print("IP client :", client_address)

response = "Jumlah karakter dalam kalimat tersebut adalah " + str(jumlahKata)

client_socket.sendall(response.encode())
client_socket.close()
server_socket.close()
```
