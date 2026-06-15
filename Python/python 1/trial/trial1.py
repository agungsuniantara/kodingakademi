# variabel = tempat menyimpan data 

buah = "apel"
print(buah)

# challange 1 : 
# 1. buat 3 variabel (nama, umur, alamat)
# 2. tampilkan 3 variabel tersebut

# tipe data (string, integer, array , float, boolean)
# string (tipe data yang berisi teks)
# integer (tipe data yang berisi angka bulat)
# float (tipe data yang berisi angka desimal)
# boolean (tipe data yang berisi nilai true/false)

contoh_string = "halo dunia"
contoh_integer = 10
contoh_float = 3.14
contoh_boolean = True

print(type(contoh_string))
print(type(contoh_integer))
print(type(contoh_float))
print(type(contoh_boolean))

contoh_float = int(contoh_float)
print(contoh_float)
print(type(contoh_float))

# challange 2 : 
# 1. buat 3 variabel dengan tipe data yang berbeda
# 2. tampilkan tipe data dari masing-masing variabel tersebut
# 3. ubah 3 variabel ke tipe data float / int / str, lalu tampilkan nilai dan tipe data barunya

# input & output 

buah = input("masukkan nama buah: ") # input
print("buah yang anda masukkan adalah " + buah) # output

# challange 3 :
# 1. buat program yang meminta user memasukkan nama, umur, dan alamat
# 2. tampilkan data yang sudah dimasukkan user dengan format :
#    "nama saya ___, umur saya ___ tahun, dan saya tinggal di ___"

# operator (aritmatika, assignment, perbandingan, logika)
# aritmatika (+, -, *, /, %, //, **) 
# assignment (=, +=, -=, *=, /=)
# perbandingan (==, !=, >, <, >=, <=)
# logika (and, or, not)

# aritmatika
a = 10
b = 3
print(a + b) # penjumlahan
print(a - b) # pengurangan
print(a * b) # perkalian
print(a / b) # pembagian
print(a % b) # sisa bagi
print(a // b) # pembulatan ke bawah
print(a ** b) # pangkat

# assignment
c = 5
c += 2 # c = c + 2
print(c)
c *= 3 # c = c * 3
print(c)
c -= 4 # c = c - 4
print(c)
c /= 2 # c = c / 2
print(c)
c %= 3 # c = c % 3
print(c)

# perbandingan
x = 10
y = 5
print(x == y) # sama dengan
print(x != y) # tidak sama dengan
print(x > y)  # lebih besar
print(x < y)  # lebih kecil
print(x >= y) # lebih besar atau sama dengan
print(x <= y) # lebih kecil atau sama dengan

# logika (and, or, not)
# and (jika kedua nilai true, maka hasilnya true)
# or (jika salah satu nilai true, maka hasilnya true)
# not (membalik nilai, jika true maka menjadi false, jika false maka menjadi true)

x = 10
y = 5
print(x == y and x != y) # false and true = false
print(x == y or x != y)  # false or true = true
print(not(x == y) and (x != y)) # true and true = true

# challange 4 :
# 1. buat 2 variabel dengan nilai integer
# 2. lakukan operasi aritmatika pada kedua variabel tersebut (semua operasi)
# 3. lakukan operasi perbandingan pada kedua variabel tersebut (semua operasi)
# 4. lakukan operasi logika pada kedua variabel tersebut (minimal 3 operasi)

# conditional statement (if, elif, else)

username = input("masukkan username: ")
password = input("masukkan password: ")

if username == "admin" and password == "12345":
    print("login berhasil")
elif username == "admin" and password != "12345":
    print("password salah")
else:
    print("username tidak ditemukan")

# challange 5 : 
# 1. buat program yang meminta user memasukkan angka
# 2. jika angka tersebut lebih dari 0, tampilkan "angka positif"
# 3. jika angka tersebut kurang dari 0, tampilkan "angka negatif"
# 4. jika angka tersebut sama dengan 0, tampilkan "angka nol"

# challange 6 :
# 1. buat program yang meminta user memasukkan nilai ujian (0-100)
# 2. jika nilai >= 80, tampilkan "A"
# 3. jika nilai >= 70 dan < 80, tampilkan "B"
# 4. jika nilai >= 60 dan < 70, tampilkan "C"
# 5. jika nilai >= 50 dan < 60, tampilkan "D"
# 6. jika nilai < 50, tampilkan "E"
# 7. jika nilai yang dimasukkan diluar rentang 0-100, tampilkan "nilai tidak valid"

# challange 7 :
# 1. buat program yang meminta user memasukkan angka
# 2. tentukan apakah angka tersebut ganjil atau genap
# 3. tampilkan hasilnya dengan format "angka ___ adalah angka ganjil/genap"




