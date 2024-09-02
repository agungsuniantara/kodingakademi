nama = "vania"
angka1 = 10 # 11
angka2 = 11
angka3 = 20
angka4 = 15
bool1 = True
bool2 = False
hasil = angka1 + angka2

print(nama)
print(f"Nama = {nama}")
print(hasil)

print(angka1)
angka1 += 1
print(angka1)

print(angka1 > angka2 and angka1 < angka3)
print(angka1 > angka2 or angka1 < angka3)

if angka1 > angka2 :
    print("kondisi true")
elif angka1 < angka4 :
    print("kondisi dua")
else:
    print("kondisi false")

for i in range(3):
    print("for 1")
    for z in range(3):
        print("for 2")

