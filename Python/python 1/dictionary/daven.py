buku = {
    "fiction" : ["marvel", "batman"],
    "drama" : ["twilight", "dynasty"]
}

kondisi = input("tambah / hapus : ")
if kondisi == "tambah":
    tipe = input("masukan jenis film : ")
    buku_baru = input("masukan buku baru : ")
    for key, value in buku.items():
        if tipe == key:
            value.append(buku_baru)
elif kondisi == "hapus":
    tipe = input("masukan jenis film : ")
    buku_hapus = input("masukan buku yang dihapus : ")
    for key, value in buku.items():
        if tipe == key:
            if buku_hapus in value:
                value.remove(buku_hapus)

print(buku)
