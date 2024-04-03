import socket
import sys
import os
import struct
import time

TCP_IP = "127.0.0.1"
TCP_PORT = 1456
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connme():
    try:
        s.connect((TCP_IP, TCP_PORT))
        print("Koneksi berhasil!")
    except:
        print("Koneksi gagal! Pastikan server telah dijalankan dan port yang digunakan benar")

def upld(file_name):
    try:
        s.send(b"upload")
    except:
        print("Tidak dapat melakukan permintaan server. Pastikan koneksi telah terhubung.")
        return
    try:
        s.recv(BUFFER_SIZE)
        s.send(struct.pack("h", sys.getsizeof(file_name)))
        s.send(file_name.encode())
        file_size = os.path.getsize(file_name)
        s.send(struct.pack("i", file_size))
        start_time = time.time()
        print("Mengirim file...")
        content = open(file_name, "rb")
        l = content.read(BUFFER_SIZE)
        while l:
            s.send(l)
            l = content.read(BUFFER_SIZE)
        content.close()
        s.recv(BUFFER_SIZE)
        s.send(struct.pack("f", time.time() - start_time))
        print("File berhasil dikirim")
        return
    except:
        print("File gagal dikirim")
        return

def list_files():
    try:
        s.send(b"ls")
    except:
        print("Tidak dapat melakukan permintaan server. Pastikan koneksi telah terhubung.")
        return
    try:
        number_of_files = struct.unpack("i", s.recv(4))[0]
        for i in range(int(number_of_files)):
            file_name_size = struct.unpack("i", s.recv(4))[0]
            file_name = s.recv(file_name_size).decode()
            file_size = struct.unpack("i", s.recv(4))[0]
            print("\t{} - {}b".format(file_name, file_size))
            s.send(b"1")
        total_directory_size = struct.unpack("i", s.recv(4))[0]
        print("Total ukuran direktori: {}b".format(total_directory_size))
    except:
        print("Tidak dapat mengambil daftar")
        return
    try:
        s.send(b"1")
        return
    except:
        print("Tidak bisa mendapatkan konfirmasi terakhir dari server.")
        return

def dwld(file_name):
    try:
        s.send(b"download")
    except:
        print("Tidak dapat melakukan permintaan server. Pastikan koneksi telah terhubung.")
        return
    try:
        s.recv(BUFFER_SIZE)
        s.send(struct.pack("h", sys.getsizeof(file_name)))
        s.send(file_name.encode())
        file_size = struct.unpack("i", s.recv(4))[0]
        if file_size == -1:
            print("File tidak tersedia. Pastikan nama file yang dimasukkan sudah benar") 
            return
    except:
        print("Error saat memeriksa file")
    try:
        s.send(b"1")
        output_file = open(file_name, "wb")
        bytes_received = 0
        print("\nProses download...")
        while bytes_received < file_size:
            l = s.recv(BUFFER_SIZE)
            output_file.write(l)
            bytes_received += BUFFER_SIZE
        output_file.close()
        print("Download berhasil {}".format(file_name))
        s.send(b"1")
        time_elapsed = struct.unpack("f", s.recv(4))[0]
        print("Waktu : {}s\nUkuran File : {}b".format(time_elapsed, file_size))
    except:
        print("File gagal didownload")
        return
    return

def delf(file_name):
    try:
        s.send(b"rm")
        s.recv(BUFFER_SIZE)
    except:
        print("Tidak dapat melakukan permintaan server. Pastikan koneksi telah terhubung.")
        return
    try:
        s.send(struct.pack("h", sys.getsizeof(file_name)))
        s.send(file_name.encode())
    except:
        print("Tidak dapat mengirim detail file")
        return
    try:
        file_exists = struct.unpack("i", s.recv(4))[0]
        if file_exists == -1:
            print("File tidak tersedia pada server")
            return
    except:
        print("Tidak dapat menentukan keberadaan file")
        return
    try:
        confirm_delete = input("Apakah anda yakin ingin menghapus? {}? (Y/N)\n".format(file_name)).upper()
        while confirm_delete != "Y" and confirm_delete != "N" and confirm_delete != "YES" and confirm_delete != "NO":
            print("Command not recognized, try again")
            confirm_delete = input("Apakah anda yakin ingin menghapus? {}? (Y/N)\n".format(file_name)).upper()
    except:
        print("Tidak dapat mengonfirmasi status penghapusan")
        return
    try:
        if confirm_delete == "Y" or confirm_delete == "YES":
            s.send(b"Y")
            delete_status = struct.unpack("i", s.recv(4))[0]
            if delete_status == 1:
                print("File berhasil dihapus")
                return
            else:
                print("File gagal dihapus")
                return
        else:
            s.send(b"N")
            print("Penghapusan dibatalkan oleh pengguna!")
            return
    except:
        print("Tidak dapat menghapus file")
        return

def get_file_size(file_name):
    try:
        s.send(b"size")
    except:
        print("Tidak dapat melakukan permintaan server. Pastikan koneksi telah terhubung.")
        return
    try:
        s.recv(BUFFER_SIZE)
        s.send(struct.pack("h", sys.getsizeof(file_name)))
        s.send(file_name.encode())
        file_size = struct.unpack("i", s.recv(4))[0]
        if file_size == -1:
            print("File tidak tersedia. Pastikan nama file yang dimasukkan sudah benar")
            return
    except:
        print("Error saat memeriksa file")
    try:
        s.send(b"1")
        print("Ukuran file : {} MB".format(file_size / 1024 / 1024))
        return
    except:
        print("Tidak bisa mendapatkan konfirmasi terakhir dari server")
        return

def quit():
    s.send(b"byebye")
    s.recv(BUFFER_SIZE)
    s.close()
    print("Koneksi server dihentikan.")
    return

print("Selamat datang dalam program FTP.\n")
print("PERINTAH :")
print("connme               : Hubungkan ke server")
print("upload <file_path>   : Upload file")
print("ls                   : List file")
print("download <file_path> : Download file")
print("rm <file_path>       : Hapus file")
print("size <file_path>     : Informasi ukuran file")
print("byebye               : Keluar program")


while True:
    prompt = input("\nMasukkan perintah : ")
    if prompt[:6].lower() == "connme":
        connme()
    elif prompt[:6].lower() == "upload":
        upld(prompt[7:])
    elif prompt.lower() == "ls":
        list_files()
    elif prompt[:8].lower() == "download":
        dwld(prompt[9:])
    elif prompt[:2].lower() == "rm":
        delf(prompt[3:])
    elif prompt[:4].lower() == "size":
        get_file_size(prompt[5:])
    elif prompt.lower() == "byebye":
        quit()
        break
    else:
        print("Perintah tidak tersedia, silahkan coba lagi")