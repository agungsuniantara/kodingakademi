# variabel = sebuah tempat untuk menyimpan data
# tipe data = jenis data yang dapat disimpan dalam variabel
# string = tipe data yang menyimpan teks
# int ( integer ) = tipe data yang menyimpan bilangan bulat
# float = tipe data yang menyimpan bilangan desimal
# boolean = tipe data yang menyimpan nilai true atau false

nama = "agung" # string
umur = 25 # int
tinggi = 175.5 # float
is_student = True # boolean

print("nama saya : ", nama)
print("Umur:", umur)
print("Tinggi:", tinggi)
print("Apakah saya seorang mahasiswa?", is_student)

print("tipe data nama:", type(nama))
print("tipe data umur:", type(umur))
print("tipe data tinggi:", type(tinggi))
print("tipe data is_student:", type(is_student))

umur = float(umur)
tinggi = int(tinggi)
print("umur setelah diubah:", umur)
print("tipe data umur setelah diubah:", type(umur))
print("tinggi setelah diubah:", tinggi)
print("tipe data tinggi setelah diubah:", type(tinggi))