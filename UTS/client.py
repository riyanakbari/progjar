import socket
import threading
import sys
import select

# Inisialisasi socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Alamat server
server_address = ('localhost', 12345)

# Terhubung ke server
client_socket.sendto("connect".encode(), server_address)

def receive_and_send():
    while True:
        # Menerima pesan dari server
        data, _ = client_socket.recvfrom(1024)
        color_eng = data.decode().split(": ")[1]

        # Meminta input warna dalam bahasa Indonesia dari pengguna
        print("Received color:", color_eng)
        color_translation = get_input_with_timeout("Translate the color '{}' to Indonesian: ".format(color_eng), 5)

        if color_translation is None:
            print("Timeout. Wait for the next color...")
            continue

        # Kirim jawaban ke server
        client_socket.sendto(color_translation.encode(), server_address)

        # Menerima feedback dari server
        feedback, _ = client_socket.recvfrom(1024)
        print("Received feedback from server:", feedback.decode())

def get_input_with_timeout(prompt, timeout_seconds):
    print(prompt)
    inputs, _, _ = select.select([sys.stdin], [], [], timeout_seconds)
    if inputs:
        return sys.stdin.readline().strip()
    else:
        return None

# Memulai thread untuk menerima dan mengirim pesan
thread_receive = threading.Thread(target=receive_and_send)
thread_receive.start()
