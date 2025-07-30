def tambah():
    angka1 = int(input("masukan angka 1 : "))
    angka2 = int(input("masukan angka 2 : "))
    hasil = angka1 + angka2
    print(hasil)

while True: 
    kondisi = int(input("pilih menu : "))
    if kondisi == 1:
        tambah()
        