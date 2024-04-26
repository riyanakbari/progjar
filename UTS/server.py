import socket
import random
import time
import threading

# Daftar kata warna dalam bahasa Inggris dan Indonesia
color_map = {
    "red": "merah",
    "green": "hijau",
    "blue": "biru",
    "yellow": "kuning",
    "orange": "jingga",
    "purple": "ungu",
    "brown": "coklat",
    "black": "hitam",
    "white": "putih"
}

# Inisialisasi socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind ke alamat dan port tertentu
server_address = ('localhost', 12345)
server_socket.bind(server_address)

print("Server listening on {}".format(server_address))
print("Waiting connecting...")

# Menyimpan status warna yang dikirim ke setiap klien
clients_colors = {}

def send_color():
    while True:
        # Membuat salinan acak dari daftar kata warna
        colors = list(color_map.keys()).copy()
        random.shuffle(colors)

        for client_address in clients_colors.keys():
            # Mengirim kata warna acak ke setiap klien
            color_eng = colors.pop()
            clients_colors[client_address] = color_eng
            message = "Color: " + color_eng
            server_socket.sendto(message.encode(), client_address)
            print("Sending color {} to client {}".format(color_eng, client_address))

        time.sleep(10)

def receive_response():
    while True:
        # Menerima jawaban dari klien
        data, address = server_socket.recvfrom(1024)
        answer = data.decode().lower()

        if answer == "connect":
            clients_colors[address] = None
            clients.add(address)
            print("Client connected:", address)
            continue

        # Memberikan feedback
        if answer in color_map.values():
            correct_color = clients_colors[address]
            if correct_color is not None and color_map[correct_color] == answer:
                feedback = "100"
            else:
                feedback = "0"

        server_socket.sendto(feedback.encode(), address)

# Menyimpan daftar klien yang terhubung
clients = set()

# Memulai thread untuk mengirim warna
thread_send = threading.Thread(target=send_color)
thread_send.start()

# Memulai thread untuk menerima jawaban
thread_receive = threading.Thread(target=receive_response)
thread_receive.start()
