cari1 = "Gunung"
cari2 = "gunung"
ganti = "pegunungan"

data = open("file\search_data.txt", "r+")
teks = data.read()

data_baru = teks.split()

Gunung = []

for i in data_baru:
    if i == cari1 or i == cari2:
        Gunung.append(i)

print(f"jumlah data gunung = {len(Gunung)}")

for i in data_baru:
    if i == cari1 or i == cari2:
        teks = teks.replace(cari1, ganti)
        teks = teks.replace(cari1, ganti)

print(teks)