# Fungsi Cek Bilangan Prima
def cek_prima(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False

# Fungsi Cetak Bilangan Prima
def cetak_prima(n):
    for num in range(2, n+1):
        if cek_prima(num):
            print(num)

n = int(input("Masukkan Jumlah Bilangan : "))

cetak_prima(n)
