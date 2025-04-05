data = open("angka.txt", "r+")
teks = data.read()

data_baru = teks.split() # list ["101","121"]

angka_genap = []
angka_ganjil = []

for i in data_baru:
    angka = int(i)
    if angka % 2 == 0:
        angka_genap.append(angka)
    else:
        angka_ganjil.append(angka)

print(data_baru)
print(angka_genap)
print(angka_ganjil)
    