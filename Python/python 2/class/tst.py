class kucing:
    nama = "anggora"
    warna = "kuning"
    
    def tampil_nama(self):
        print(self.nama)

data = kucing()
data.tampil_nama()
print(data.nama)

class benda:
    def __init__(self, a, b):
        self.nama = a
        self.warna = b
    
    def tampil_nama(self):
        print(self.nama)

data2 = benda("meja", "cokelat")
data2.tampil_nama()
print(data2.warna)