class orang:
    nama = "rama"
    umur = 20
    
    def __init__(self, a):
        self.alamat = a
    
    def tampil(self):
        print(self.nama)
        print(self.umur)
        print(self.alamat)

data1 = orang("denpasar")
data2 = orang("badung")
data1.tampil()
data2.tampil()