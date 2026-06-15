genap = 0
ganjil = 0

with open ("angka.txt", "r") as f:
    angka = f.readlines()
    for i in angka:
        if int(i) % 2 == 0:
            genap += 1
        else:
            ganjil += 1

print(f"Jumlah angka genap: {genap}")
print(f"Jumlah angka ganjil: {ganjil}")