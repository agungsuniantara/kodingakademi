class pegawai:
    def __init__(self, a,b,c,d):
        self.nama = a
        self.status = b 
        self.tahun = c 
        self.gaji = d 

class data:
    def __init__(self):
        self.dict = {}
    
    def tambah(self, karyawan):
        nama = karyawan.nama
        self.dict[nama] = karyawan
    
    def edit(self, search, data_baru):
        for key, value in self.dict.items():
            if key == search:
                value.status = data_baru["status"]
                value.tahun = data_baru["tahun"]
                value.gaji = data_baru["gaji"]
    
    def hapus(self, search):
        for key in self.dict.copy():
            if key == search:
                self.dict.pop(search)
    
    def tampil(self):
        for key, value in self.dict.items():
            print("Nama : ", key)
            print("Status : ", value.status)
            print("Tahun : ", value.tahun)
            print("Gaji : ", value.gaji)
    
    def menu(self):
        print("Silahkan memilih menu : ")
        print("1. Tambah Pegawai")
        print("2. Edit Pegawai")
        print("3. Hapus Pegawai")
        print("4. Tampilkan Pegawai")
        print("5. Keluar Sistem")

database = data()

while True :
    database.menu()
    pilih = int(input("masukan pilihan : "))
    if pilih == 1:
        nama = input("masukan nama : ")
        status = input("masukan status : ")
        tahun = input("masukan tahun : ")
        gaji = input("masukan gaji : ")
        karyawan = pegawai(nama, status, tahun, gaji)
        database.tambah(karyawan)
    elif pilih == 2:
        nama = input("Masukan nama edit : ")
        status = input("masukan status : ")
        tahun = input("masukan tahun : ")
        gaji = input("masukan gaji : ")
        df = dict(status = status, tahun = tahun, gaji = gaji)
        database.edit(nama, df)
    elif pilih == 3:
        nama = input("Masukan nama hapus : ")
        database.hapus(nama)
    elif pilih == 4:
        database.tampil()
    elif pilih == 5:
        break
        







# pegawai1 = pegawai("yani", "tetap", "2020", "10")

# data1 = data()
# data1.tambah(pegawai1)

# baru = {
#     "status" : "part time",
#     "tahun" : "2021",
#     "gaji" : "20"
# }

# data1.edit("yani", baru)
# data1.hapus("yani")
# data1.tampil()
