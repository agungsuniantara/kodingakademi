from test import tambah

# Menggunakan fungsi tambah dari test.py
hasil_tambah = tambah(5, 15)
print("Hasil penjumlahan:", hasil_tambah)

# Menggunakan lambda function
hasil_lambda = (lambda x, y: x + y)(5, 15)
print("Hasil lambda:", hasil_lambda)

class orang:
    def __init__(self, a, b, c) :
        self.nama = a
        self.umur = b
        self.alamat = c
    
    def tampil_nama(self):
        print(f"nama = {self.nama}")
    def tampil_umur(self):
        print(f"umur = {self.umur}")
    def tampil_alamat(self):
        print(f"alamat = {self.alamat}")
        
data1 = orang("william", "12 tahun", "denpasar")
data2 = orang("wahyu", "13 tahun", "tabanan")

data1.tampil_nama()
data2.tampil_nama()




    