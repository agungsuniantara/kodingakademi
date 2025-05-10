data = {
    "nama" : "gadis", # key : value
    "alamat" : "denpasar",
    "list" : [1,2,3,4,5]
}

print(data["nama"])
print(data["list"])

# len

jumlah = len(data)
print(jumlah)

# get

tidak_ketemu = data.get("baru", "key tidak ditemukan")
ketemu = data.get("nama", "key tidak ditemukan")

print(tidak_ketemu)
print(ketemu)

# update (update data, jika key tidak ketemu maka jadi data baru)

data["nama"] = "ucup" # data diganti langsung dengan key
print(data["nama"])

data.update({"baru":"hello"})
print(data)

# del (menghapus data dengan key)

del data["baru"]
print(data)

# copy (duplikat data)

baru = data.copy()
print(baru)

# pop (menghapus data dengan key namun value bisa disimpan)

print(data)
test = data.pop("nama")
print(data)
print(test)

# popitem (memindahkan data akhir pada variabel baru)

data = {
    "nama" : "gadis",
    "alamat" : "denpasar"
}

data_akhir = data.popitem()
print(data_akhir) # ("alamat", "denpasar")

# clear (menghapus semua data)

data = {
    "nama" : "gadis",
    "alamat" : "denpasar"
}

data.clear()
print(data)

# keys (mengambil data key pada dictionary)

data = {
    "nama" : "gadis",
    "alamat" : "denpasar"
}

key_list = data.keys()
print(key_list)

# items (mengambil data key dan value pada dictionary)

data = {
    "nama" : "gadis",
    "alamat" : "denpasar"
}

items_list = data.items()
print(items_list)

# values (mengambil data value pada dictionary)

data = {
    "nama" : "gadis",
    "alamat" : "denpasar"
}

value_list = data.values()
print(value_list)

# setdefault (mencari value data key, jika tidak ditemukan maka akan dibuat baru)

data = {
    "nama" : "gadis",
    "alamat" : "denpasar"
}

ketemu = data.setdefault("nama", "wahyu")
print(ketemu)
tidak_ketemu = data.setdefault("baru", "test")
print(data)
print(tidak_ketemu)

# fromkeys (membuat dictionary baru dengan key berbeda dan value yang sama)

key = ["data1", "data2", "data3"]
value = "unknown"

new = dict.fromkeys(key, value)
print(new)

new2 = dict(nama="gadis", umur=20)
print(new2)
