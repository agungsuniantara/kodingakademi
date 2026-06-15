class mahasiswa:
    def __init__(self):
        self.data = {} # {nim: [nama, alamat], nim: [nama, alamat]}
    
    def tambah(self, nama, nim, alamat):
        self.data[nim] = [nama, alamat] # {nim: [nama, alamat], nim: [nama, alamat]}
    
    def tampil(self):
        for nim, info in self.data.items(): # nim = nim , info = [nama, alamat]
            print(f"NIM: {nim}, Nama: {info[0]}, Alamat: {info[1]}")
    
database = mahasiswa()

for i in range(5):
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    alamat = input("Masukkan alamat mahasiswa: ")
    database.tambah(nama, nim, alamat)

database.tampil()

print(database.data["12345"]) # Output: ['Nama Mahasiswa', 'Alamat Mahasiswa']
