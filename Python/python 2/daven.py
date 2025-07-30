class karyawan:
    def __init__(self):
        self.data = {}
    
    def tambah_data(self, nama, status, tahun, gaji):
        self.data[nama] = [status, tahun, gaji]
        
    def edit_data(self, nama):
        for key, value in self.data.items():
            if key == nama:
                status = input("status baru : ")
                tahun = input("tahun baru : ")
                gaji = input("gaji baru : ")
                value[0] = status
                value[1] = tahun
                value[2] = gaji
              
    def tampil_data(self):
        for key, value in self.data.items():
            print("Data karyawan : ")
            print(f"nama pegawai : {key}")
            print(f"status kerja : {value[0]}")
            print(f"tahun masuk : {value[1]}")
            print(f"gaji : {value[2]}")

data = karyawan()

pilih = input("masukan pilihan : ")
if pilih == 1:
    nama = input("masukan nama : ")
    status = input("masukan status : ")
    tahun = input("masukan tahun : ")
    gaji = input("masukan gaji : ")
    data.tambah_data(nama, status, tahun, gaji)
