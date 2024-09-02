def cek_angka(bilangan):
    if bilangan >= 0:
        return "positif"
    else:
        return "negatif"

positif = []
negatif = []

print("masukan 10 buah angka !")

for i in range(10):
    bilangan = int(input(f"masukan angka {i + 1} :"))
    cek = cek_angka(bilangan)

    if cek == "positif":
        positif.append(bilangan)
    else:
        negatif.append(bilangan)

print(f"bilangan positif = {positif}")
print(f"bilangan positif = {negatif}")
