# class default

class manusia:
    nama = "gadis"
    umur = 50
    alamat = "denpasar"
    
    def tampil_nama(self):
        print(f"nama = {self.nama}")
    def tampil_umur(self):
        print(f"umur = {self.umur}")
    def tampil_alamat(self):
        print(f"alamat = {self.alamat}") 

data = manusia()
print(data.nama)
print(data.umur)
print(data.alamat)
data.tampil_alamat()

# class konstruktor

class user:
    def __init__(self, a, b, c): # konstruktor
        self.nama = a 
        self.alamat = b 
        self.umur = c
    
    def tampil_data(self):
        print(f"nama = {self.nama}")
        print(f"alamat = {self.alamat}")
        print(f"umur = {self.umur}")

data1 = user("agung", "denpasar", "26 tahun")
data2 = user("gadis", "denpasar", "20 tahun")

print("class konstruktor : ")
data1.tampil_data()
data2.tampil_data()

# class inheritance (pewarisan)

class mahasiswa:
    def __init__(self, a, b, c, d):
        self.nim = a
        self.nama = b 
        self.email = c 
        self.alamat = d 
    
    def tampil_data(self):
        print(f"nim = {self.nim}")
        print(f"nama = {self.nama}")
        print(f"email = {self.email}")
        print(f"alamat = {self.alamat}")

class matkul(mahasiswa):
    def __init__(self, a, b, c, d, e):
        super().__init__(a, b, c, d)
        self.nama_matkul = e 
    
    def tampil_matkul(self):
        print(f"nama matkul : {self.nama_matkul}")

data1 = matkul("1234", "gadis", "gadis@gmail.com", "denpasar", "praktikum")
print("class inheritance : ")
print(data1.nim)
data1.tampil_data()
data1.tampil_matkul()

# class dictionary

class data: 
    def __init__(self):
        self.df = {}
    
    def tambah_data(self, nim, nama, alamat, umur):
        self.df[nim] = [nama, alamat, umur]
    
    def tampil(self):
        for key, value in self.df.items():
            print("data mahasiswa : ")
            print(f"nim = {key}")
            print(f"nama = {value[0]}")
            print(f"alamat = {value[1]}")
            print(f"umur = {value[2]}")

test = data()
test.tambah_data("1234", "gadis", "denpasar", "20 tahun")
test.tambah_data("222", "wayan", "denpasar", "20 tahun")
test.tambah_data("333", "agus", "denpasar", "20 tahun")
test.tampil()