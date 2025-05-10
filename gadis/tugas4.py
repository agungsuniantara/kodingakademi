def penjumlahan (a, b):
    return a + b

def pengurangan (a, b):
    return a - b

def perkalian (a, b):
    return a * b

def pembagian(a, b):
    if b != 0:
        return a / b
    else:
        return "tidak bisa dibagi dengan nol"

def menu():
    print("Silahkan memilih menu : ")
    print("1. penjumlahan")
    print("2. pengurangan")
    print("3. perkalian")
    print("4. pembagian")

while True :
    menu()
    pilihan = int(input("masukan pilihan : "))
    if pilihan == 1:
        angka1 = int(input("masukan angka 1 : "))
        angka2 = int(input("masukan angka 2 : "))
        hasil = penjumlahan(angka1, angka2)
        print(f"hasil penjumlahan : {hasil}")
    elif pilihan == 2:
        angka1 = int(input("masukan angka 1 : "))
        angka2 = int(input("masukan angka 2 : "))
        hasil = pengurangan(angka1, angka2)
        print(f"hasil pengurangan : {hasil}")
    elif pilihan == 3:
        angka1 = int(input("masukan angka 1 : "))
        angka2 = int(input("masukan angka 2 : "))
        hasil = perkalian(angka1, angka2)
        print(f"hasil perkalian : {hasil}")
    elif pilihan == 4:
        angka1 = int(input("masukan angka 1 : "))
        angka2 = int(input("masukan angka 2 : "))
        hasil = pembagian(angka1, angka2)
        print(f"hasil pembagian : {hasil}")
    else:
        print("pilihan tidak tersedia")
    
    kondisi = input("masih ingin memilih ? ")
    if kondisi.lower() == "tidak":
        break
        