####=========Mini Project Calculator=========####

##==Buat Input dan Variabelnya==##

angka1 = int(input("Masukkan angka pertama "))
angka2 = int(input("Masukkan angka kedua "))

print("List Operasi")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Pembagian")
print("4. Perkalian")

##==Buat Input Operasi==##
operasi = int(input("Masukkan Operasi "))

##==Buat Logika ketika operasi dimasukkan==##
if operasi == 1:
    hasil = angka1 + angka2
elif operasi == 2:
    hasil = angka1 - angka2
elif operasi == 3:
    hasil = angka1 * angka2
elif operasi == 4:
    hasil = angka1 / angka2
else :
    hasil = "operasi diluar 4 itu tidak ada"

##==Buat Output yang diinginkan==##
print("Hasil operasi : ", hasil)