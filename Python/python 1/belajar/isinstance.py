data = [10, 12, 5, 13]

# contoh 1 ( tidak pakai function ) :

for item in data:
    if isinstance(item, int):
        print("angka")

# contoh 1 ( pakai function ) :

def cek(x):
    if isinstance(x, int):
        print("angka")

for item in data:
    cek(item)

# contoh 2 :

def cek2(x):
    if x in data:
        print(f"terdapat {x} pada data list")

cek2(10)

# assignment : 

data2 = [10, 12, 5, 13, 'hallo']

hasil_akhir = []

for item3 in data2:
    if not isinstance(item3, str):
        hasil_akhir.append(item3)
    else:
        hasil_akhir.append(None)

print(hasil_akhir)

# pakai function

def cek3(x):
    if isinstance(x, str):
        return None
    else:
        return x

hasil = [cek3(item3) for item3 in data2]
print(hasil)










