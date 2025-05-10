# inisialisasi list
data = [1,2,3,4,5]
data_string = ["a", "b", "c"]
data_bool = [False, True]
data_campur = [1, "a", True]

print(data)
print(data_string)
print(data_bool)
print(type(data_campur))

# akses list

# index = [0,1,2,3,5]
# index = [-5, -4, -3, -2, -1]
data = ["a","b","c","d","e"]

print(data[0])
print(data[1])
print(data[-1])
print(data[-2])

# slicing
print(data[0:3]) # [start : batas]
print(data[-4:]) # [start : batas]

# fungsi cek jumlah data
data = ["a","b"]
print(len(data))

# fungsi menambah data
data = ["a","b","c"]

data.insert(1, "halo") # insert (menambahkan data sesuai index)
print(data)
data.append("test") # append (menambahkan data di belakang)
print(data)

data2 = ["d","e","f"]
data.extend(data2) # extend (menambahkan data berupa list)
print(data)

# merubah data
data = ["a","b"]
data[1] = "hiu"
print(data)

# menghapus data
data = ["a","b","moo"]

data.remove("moo") # remove menghapus data sesuai dengan valuenya
print(data)

simpan = data.pop(1) # pop menghapus data dengan index sekaligus 'bisa' menyimpan data hapus
print(simpan)
print(data)

data.clear() # menghapus semua data
print(data)

# beberapa fungsi list
data = [30, 40, 50, 10, 10]

angka10 = data.count(10) # count (menghitung banyak value yang di cari)
print(angka10) 
index40 = data.index(40) # index (mencari index dari value yang dicari)
print(index40)
data.sort() # sort (mengurutkan data dari terkecil ke terbesar)
print(data) 
data.reverse() # reverse (membalikkan data)
print(data)

# Assignment

# 1. buat sebuah list kosong.
# 2. buat variabel input nama, alamat, umur, nim, jurusan.
# 3. masukkan setiap data pada list.
# 4. kemudian tampilkan semua data pada list dengan index dan slicing.

data = []

nama = input("masukan nama : ")
alamat = input("masukan alamat : ")
umur = input("masukan umur : ")
nim = input("masukan nim : ")
jurusan = input("masukan jurusan : ")

data.append(nama)
data.append(alamat)
data.append(umur)
data.append(nim)
data.append(jurusan)

print(f"nama = {data[0]}")
print(f"alamat = {data[1]}")
print(f"umur = {data[2]}")
print(f"nim = {data[3]}")
print(f"jurusan = {data[4]}")

print(f"data = {data[0:]}")


