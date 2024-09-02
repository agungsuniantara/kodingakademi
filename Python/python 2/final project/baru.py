class pegawai:
    def __init__(self, a, b, c, d):
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
    
    def tampil(self):
        for key, value in self.dict.items():
            print(f"Nama : {key}")
            print(f"Status : {value.status}")
            print(f"tahun : {value.tahun}")
            print(f"gaji : {value.gaji}")

pegawai1 = pegawai("guspram", "karyawan tetap", "2010", "10")

data1 = data()
data1.tambah(pegawai1)

baru = {
    "status" : "part time", 
    "tahun" : "2001",
    "gaji" : "50"
}

data1.edit("guspram", baru)
data1.tampil()
        
        

