# membuat list
hewan = ["Sapi", "Ayam", "Kambing", "Kuda"]
item_list = ["Book", 23, 1984, True, "Pencil"]

for h in hewan:
    print(h, end=" ")
print()
for item in item_list:
    print(item, end=" ")

print()
print()

# mengambil nilai dari list
hewan = ["Sapi", "Ayam", "Kambing", "Kuda"]

"Mengambil Data Pertama"
print(hewan[0])

"Mengambil Data Kedua"
print(hewan[1])

"Mengambil Data Ketiga"
print(hewan[2])

"Mengambil Data Keempat"
print(hewan[3])

print()

# mengganti nilai list
hewan = ["Sapi", "Ayam", "Kambing", "Kuda"]
print("Sebelum diubah")
print(hewan[0])
hewan[0] = "Kangguru"
print("Setelah diubah")
print(hewan[0])

print()

#append menambahkan item dari belakang
colors = ["Red", "Blue", "Green"]
colors.append("Brown")
for i in colors:
    print(colors)

#insert menambahkan item dari index tertentu
colors = ["Red", "Blue", "Green"]
colors.insert(0, "Brown")
for i in colors:
    print(colors)

print()

#menghapus item
colors = ["Red", "Blue", "Green"]
del colors[1]
print(colors)
colors = ["Red", "Blue", "Green"]
colors.remove("Blue")
print(colors)

print()

#operasi penggabungan list
hewan = ["Gajah", "Kucing", "Tikus", "Anjing"]
tumbuhan = ["Putri Malu", "Lidah Buaya", "Mangga"]
makhluk_hidup = hewan + tumbuhan
print(makhluk_hidup)

print()

#operasi perkalian list
hewan = ["Gajah", "Kucing", "Tikus", "Anjing"]
makhluk_hidup = hewan * 5
print(makhluk_hidup)

print()

#list multidimensi
minuman =[
    ["Kopi", "Susu", "Teh"],
    ["Jus Apel", "Jus Melon", "Jus Jeruk"],
    ["Es Kopi", "Es Campur", "Es Teler"]
]

#manggil data list multidimensi
print(minuman[0][0])
print()
for list in minuman:
    for menu in list:
        print(menu,end=", ")
    print()

print()

#mengetahui jumlah data / panjang list
hewan = ["Gajah", "Kucing", "Tikus", "Anjing"]
print("panjang list hewan adalah = ", len(hewan))