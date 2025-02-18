class karyawan:
    def __init__(self):
        self.dict = {}
    
    def tambah(self, nama, status, tahun, gaji):
        self.dict[nama] = [status, tahun, gaji]
    
    def tampil(self):
        nomer = 1
        for key, value in self.dict.items():
            print(f"Data {nomer} : ")
            print(f"Nama = {key}")
            print(f"Status = {value[0]}")
            print(f"Tahun = {value[1]}")
            print(f"Gaji = {value[2]}")
            nomer += 1
    
    def edit(self, search, data_baru):
        for key, value in self.dict.items():
            if key == search:
                value[0] = data_baru[0]
                value[1] = data_baru[1]
                value[2] = data_baru[2]
    
    def hapus(self, search):
        for key in self.dict.copy().keys():
            if key == search:
                self.dict.pop(search)
    
    def menu(self):
        print("Selamat datang di sistem informasi pegawai : ")
        print("Silahkan memilih menu : ")
        print("1. Tambah Pegawai")
        print("2. Edit pegawai")
        print("3. Hapus pegawai")
        print("4. Tampilkan pegawai")
        print("5. Keluar sistem")
        
data = karyawan()

while True :
    data.menu()
    
    pilih = int(input("masukan pilihan : "))
    if pilih == 1:
        nama = input("masukan nama = ")
        status = input("masukan status = ")
        tahun = input("masukan tahun = ")
        gaji = input("masukan gaji = ")
        data.tambah(nama, status, tahun, gaji)
    elif pilih == 2:
        nama = input("masukan nama edit = ")
        status = input("masukan status = ")
        tahun = input("masukan tahun = ")
        gaji = input("masukan gaji = ")
        data_edit = [status, tahun, gaji]
        data.edit(nama, data_edit)
    elif pilih == 3:
        nama = input("masukan nama hapus = ")
        data.hapus(nama)
    elif pilih == 4:
        data.tampil()
    elif pilih == 5:
        break
    
    


