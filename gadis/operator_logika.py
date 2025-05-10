angka1 = 10
angka2 = 20
angka3 = 30

# & (and)
# -- jika salah satu kondisi bernilai false
# -- maka hasilnya pasti false

print((angka1 < angka2) & (angka1 > angka3) & (angka3 < angka2))

# | (or)
# -- jika salah satu kondisi bernilai true
# -- maka hasilnya pasti true

print((angka1 < angka2) | (angka1 > angka3) | (angka3 < angka2))

# ! (not)
# -- kebalikan jika digunakan pada kondisi true
# -- maka akan menjadi false

print(not(angka1 < angka2) | (angka1 > angka3) | (angka3 < angka2))