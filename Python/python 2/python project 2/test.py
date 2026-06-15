class karyawan:
    def __init__(self, a, b, c):
        self.nama = a
        self.alamat = b
        self.umur = c

class kantor:
    def __init__(self):
        self.data = {}
    
    def tambah_data(self, user):
        nama = user.nama 
        self.data[nama] = user
    
    def tampil_dictionary(self):
        print(self.data)

user1 = karyawan("guspram", "denpasar", 20)

guspram = kantor()
guspram.tambah_data(user1)