nama = "celyn"
alamat = "jl suka no D55"
umur = 20

# print() digunakan untuk menampilkan output ke terminal
print("nama saya adalah", nama) 
print("alamat saya adalah", alamat)
print("umur saya adalah", umur)

# data types(int, float, str, bool)
# int = bilangan bulat
# float = bilangan desimal
# str = string (teks)
# bool = boolean (true/false)

kata = "hello world" # string
angka = 10 # integer
desimal = 3.14 # float
benar = True # boolean

print("kata:", kata, "type:", type(kata))
print("angka:", angka, "type:", type(angka))
print("desimal:", desimal, "type:", type(desimal))
print("benar:", benar, "type:", type(benar))

# konversi tipe data
angka = float(angka) # konversi int ke float
print("angka setelah konversi:", angka, "type:", type(angka))

desimal = int(desimal) # konversi float ke int
print("desimal setelah konversi:", desimal, "type:", type(desimal))

# input / output

nama = input("masukan nama : ")
print("nama yang dimasukan adalah", nama)

# operator (aritmatika, assignment, perbandingan, logika)
# aritmatika: +, -, *, /, %, **, //
# assignment: =, +=, -=, *=, /=, %=, **=
# perbandingan: ==, !=, >, <, >=, <=
# logika: and, or, not

# aritmatika

a = 10
b = 3
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print("a // b =", a // b)

word1 = "koding"
word2 = "akademi"
word3 = word1 + " " + word2
print("hasil penggabungan string:", word3)

# assignment

x = 5
print("nilai x:", x) # 5
x += 2 # x = x + 2
print("nilai x setelah ditambah 2:", x) # 7
x *= 3 # x = x * 3
print("nilai x setelah dikalikan 3:", x) # 21
x /= 2
print("nilai x setelah dibagi 2:", x)
x %= 4
print("nilai x setelah di modulus 4:", x)
x **= 2
print("nilai x setelah dipangkatkan 2:", x)

# comparison / perbandingan ( true / false )

y = 10
z = 20
print("y == z:", y == z) # False, == (sama dengan)
print("y != z:", y != z) # True, != (tidak sama dengan)
print("y > z:", y > z) # False, > (lebih besar dari)
print("y < z:", y < z) # True, < (lebih kecil dari)
print("y >= z:", y >= z) # False, >= (lebih besar atau sama dengan)
print("y <= z:", y <= z) # True, <= (lebih kecil atau sama dengan)

angka1 = input("masukan angka : ")
print("angka :", angka1, "type:", type(angka1)) # input selalu menghasilkan string

angka2 = int(input("masukan angka : "))
print("angka :", angka2, "type:", type(angka2)) # konversi input ke int

# logika (and, or, not)
# and = true jika kedua kondisi benar
# or = true jika salah satu kondisi benar
# not = negasi (membalik nilai)

a = 10
b = 20
c = 30

print("a > 5 and b < 25:", (a > 5 and b < 25)) # True and True = True
print("a > 15 or b < 25:", (a > 15 or b < 25)) # False or True = True
print("not a > 5:", not(a > 5)) # not True = False


