###===Buat Kode agar menghasilkan tampilan seperti berikut===###

#                         *
#                         **
#                         ***
#                         ****
#                         *****

###===Step 1 : Buat output mengasilkan seperti ini===###
#                           0
#                           1
#                           2
#                           3
#                           4

# panjang = 5
# for i in range(panjang):
#     print(i)

###===Step 2 : Buat output menghasilkan bintang sesuai angka ===###
# jika lebar = 3 maka menampilkan : ***

# lebar = 3
# for i in range(lebar):
#     print("*", end="")

###===Step 3 : kombinasikan semuanya===###

panjang = 5
for i in range(panjang):
    for a in range(i):
        print("*", end="")
    print("")