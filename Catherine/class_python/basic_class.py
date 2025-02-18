class data:
    def __init__(self, angka):
        self.angka = angka

class bangun_ruang :
    angka1 = 100
    angka2 = 200
    angka_10 = []

    def __init__(self, angka3):
        self.angka3 = angka3

    def tambah(self):
        hasil = self.angka1 + self.angka2 + self.angka3
        return hasil

    def tambah2(self):
        hasil = self.angka1 + self.angka2 + self.angka3
        print(hasil)

    def tambah4(self, angka4):
        self.angka_10.append(angka4)
        hasil = self.angka1 + self.angka2 + self.angka3
        print(hasil)

    def tampil(self):
        """
        Menampilkan isi dari angka_10.
        """
        print("Isi angka_10:")
        for idx, obj in enumerate(self.angka_10):
            print(f"{idx + 1}. {obj.angka}")


data1 = bangun_ruang(30)
data2 = bangun_ruang(40)

print(data1.angka1) # call atribut
print(data1.angka2) # call atribut

total = data1.tambah()
print(total)

data1.tambah2()
data2.tambah4(data1)
data2.tampil()