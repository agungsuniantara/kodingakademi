# no 1
data = {
    "nama" : input("masukan nama : "),
    "alamat" : input("masukan alamat : "),
    "umur" : input("masukan umur : ")
}

print(f"Nama : {data['nama']}")
print(f"Alamat : {data['alamat']}")
print(f"Umur : {data['umur']}")

# no 2
buku = {
    "action" : "harry potter", 
    "romance" : "cinta fitri", 
    "drama" : "tukang bubur naik haji"
}

buku.update({"thriller" : "halloween"}) # menambah buku
print(buku)
value = buku.pop("romance")
print(buku)
print(value)