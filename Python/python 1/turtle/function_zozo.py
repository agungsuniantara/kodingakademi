def menu():
    print("silahkan memilih menu : ")
    print("1. penjumlahan")
    print("2. pengurangan")
    print("3. perkalian")
    print("4. pembagian")

def tambah():
    angka1 = int(input("masukan angka 1 : "))
    angka2 = int(input("masukan angka 2 : "))
    hasil = angka1 + angka2 
    print(hasil)
    
while True : 
    menu()
    
    pilih = input("masukan pilihan : ")
    
    if pilih == "1":
        tambah()
    
    kondisi = input("apakah masih ingin mengulang ? ")
    if kondisi == "tidak":
        break