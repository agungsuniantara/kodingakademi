class karyawan:
    def __init__(self):
        self.dict = {}
    
    def create(self, nama, status, tahun, gaji):
        self.dict[nama] = [status, tahun, gaji]
    
    def read(self):
        for key, value in self.dict.items():
            print(f"Nama = {key}")
            print(f"Status = {value[0]}")
            print(f"Tahun = {value[1]}")
            print(f"Gaji = {value[2]}")
    
    def edit(self, search, data_baru):
        for key, value in self.dict.items():
            if key == search:
                value[0] = data_baru[0]
                value[1] = data_baru[1]
                value[2] = data_baru[2]
    
    def hapus(self, search):
        for key, value in self.dict.items():
            if key == search:
                self.dict.pop(search)
    
    def menu(self):
        print("Selamat datang di sistem informasi pegawai : ")
        print("Silahkan memilih menu : ")
        print("1. Tambah Pegawai")
        print("2. Edit pegawai")
        print("3. Hapus pegawai")
        print("4. Tampilkan pegawai")
        
data = karyawan()

while True :
    data.menu()
    
    pilih = int(input("masukan pilihan : "))
    
    if pilih == 2:
        nama = input("masukan nama edit = ")
        status = input("masukan status = ")
        tahun = input("masukan tahun = ")
        gaji = input("masukan gaji = ")
        
        data_edit = [status, tahun, gaji]
        data.edit(nama, data_edit)

# data.create(nama, "fulltime", "2020", "100000000")
# data.read()

# nama = input("masukan nama edit = ")
# status = input("masukan status = ")
# tahun = input("masukan tahun = ")
# gaji = input("masukan gaji = ")

# data_edit = [status, tahun, gaji]

# data.edit(nama, data_edit)
# data.read()