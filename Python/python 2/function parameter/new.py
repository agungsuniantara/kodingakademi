def tambah():
    angka1 = int(input("angka 1 : "))
    angka2 = int(input("angka 2 : "))
    hasil = angka1 + angka2
    print(f"hasil = {hasil}")

def kali():
    angka1 = int(input("angka 1 : "))
    angka2 = int(input("angka 2 : "))
    hasil = angka1 * angka2
    print(f"hasil = {hasil}")

def kurang():
    angka1 = int(input("angka 1 : "))
    angka2 = int(input("angka 2 : "))
    hasil = angka1 - angka2
    print(f"hasil = {hasil}")

def bagi():
    angka1 = int(input("angka 1 : "))
    angka2 = int(input("angka 2 : "))
    hasil = angka1 / angka2
    print(f"hasil = {hasil}")

while(True):
    print("kalkulator sederhana")
    kondisi = input("pilih +, -, *, / : ")
    if kondisi == "+":
        tambah()
    elif kondisi == "-":
        kurang()
    tanya = input("apakah ingin mengulang lagi ? ")
    if tanya == "tidak":
        break