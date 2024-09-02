class mahasiswa:
    def __init__(self):
        self.data = {}
    
    def tambah(self, nama, nim, usia, jurusan, alamat):
        value = [nim, usia, jurusan, alamat]
        key = nama
        self.data[key] = value
    
    def tampil(self):
        for key, value in self.data.items():
            print(f"Nama : {key}")
            print(f"Nim : {value[0]}")
            nim = value[0]
            tahun = "20" + nim[0] + nim[1]
            print(f"Tahun : {tahun}")
            
yani = mahasiswa()
yani.tambah("yani", "17990", "20 tahun", "sistem informasi", "denpasar")
yani.tampil()