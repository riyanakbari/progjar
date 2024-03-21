# Membuat program untuk menghitung jumlah huruf dalam sebuah kata yang dimasukkan pengguna.

kata = input("Masukkan kata : ")

jumlah = len(kata)

print("Jumlah huruf dalam kata {} tersebut adalah : {}" .format(kata,jumlah))

#  Membuat program untuk menghitung luas dan keliling lingkaran dengan input jari-jari dari pengguna.

jari = float(input("Masukkan Jari - Jari Lingkaran :"))

luas = 3.14 * jari * jari

keliling = 2 * 3.14 * jari

print("Luas Lingkaran : {:.2f}" .format(luas))
print("Keliling Lingkaran : {:.2f}" .format(keliling))

#  Membuat program untuk mengubah suhu dari Fahrenheit ke Celsius atau sebaliknya.

print("Pilih tipe input (celcius / farenheit)")
print("1. Celcius \n2. Farenheit")
menu = input("Masukkan pilihan: ")

if menu == '1':
    suhu = float(input("Masukkan Suhu Celcius: "))
    convert = 9/5 * suhu + 32
    print("Suhu Fahrenheit adalah {:.2f}".format(convert))
elif menu == '2':
    suhu = float(input("Masukkan Suhu Fahrenheit: "))
    convert = 5/9 * (suhu - 32)
    print("Suhu Celcius adalah {:.2f}".format(convert))
else:
    print("Pilihan tidak valid")
