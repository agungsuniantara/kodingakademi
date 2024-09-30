buku = {
    "fiction" : ["marvel", "batman"],
    "drama" : ["twilight", "dynasty"]
}

tipe = input("masukan jenis film : ")
buku_baru = input("masukan buku baru : ")
for key, value in buku.items():
    if tipe == key:
        value.append(buku_baru)

print(buku)
