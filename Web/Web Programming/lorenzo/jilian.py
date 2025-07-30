def tambah(angka1, angka2):
    hasil = angka1 + angka2 
    return hasil

while True:
    print("Menu : ")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    
    pilih = input("masukan pilihan : ")
    if pilih == "1":
        angka1 = input("masukan angka 1 : ")
        angka2 = input("masukan angka 2 : ")
        result = tambah(angka1, angka2)
        print(result)
    
    kondisi = input("masih ingin memilih ? ")
    if kondisi == "tidak":
        break
    