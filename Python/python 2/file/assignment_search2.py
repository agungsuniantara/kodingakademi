cari = "gunung"
ganti = "pegunungan"

data = open("/Applications/MAMP/htdocs/local/kodingakademi/Python/python 2/file/search_data.txt", "r+")
teks = data.read()

data_baru = teks.split()

Gunung = []

for i in data_baru:
    if i.lower() == cari:
        Gunung.append(i)

print(f"jumlah data gunung = {len(Gunung)}")

for i in data_baru:
    if i.lower() == cari:
        teks = teks.replace(cari, ganti)

print(teks)