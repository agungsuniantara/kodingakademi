class user:
       def __init__(self, a,b,c):
              self.nama = a
              self.alamat = b
              self.umur = c
       
       def panggil_nama(self):
              print(self.nama)
0
class manager(user):
       def __init__(self, a, b, c, d):
              super().__init__(a, b, c)
              self.jabatan = d
       
       def panggil_jabatan(self):
              print(self.jabatan)

class staff(user):
       def __init__(self, a, b, c, d):
              super().__init__(a, b, c)
              self.jabatan = d
       
       def panggil_jabatan(self):
              print(self.jabatan)

guspram = manager("guspram", "denpasar", 20, "manager")
agung = staff("guspram", "denpasar", 20, "staf")
guspram.panggil_nama()
guspram.panggil_jabatan()
agung.panggil_nama()
agung.panggil_jabatan()


