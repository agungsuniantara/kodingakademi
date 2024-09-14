class Mahasiswa:
    def __init__(self):
        self.dict = {}
        
    def daftar(self,nama, nim, usia, jurusan, alamat):
        tahun = f"20{nim[0:2]}"
        self.dict[nim] = {nama, usia, jurusan, alamat, tahun}
    
    def tampil(self):
        for key,value in self.dict.items():
            print("Data : ")
            print(f"Nim : {key}")
            print(f"Data : {value}")

mahasiswa = Mahasiswa()
mahasiswa.daftar("agus", "198888", "20 tahun", "sistem informasi", "denpasar")
mahasiswa.tampil()
