class Mahasiswa:
    def __init__(self, nama, nim, usia, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.usia = usia
        self.jurusan = jurusan
        self.alamat = alamat

class DaftarMahasiswa:
    def __init__(self):
        self.dict = {}

    def tambah(self, mahasiswa):
        nim = mahasiswa.nim
        self.dict[nim] = mahasiswa

    def tampil(self):
        print("daftar mahasiswa : ")
        no = 1
        for nim, data in self.dict.items():
            print(f"data {no}")
            print(f"nim : {nim}")
            print(f"nama = {data.nama}")
            print(f"usia = {data.usia}")
            print(f"jurusan = {data.jurusan}")
            print(f"alamat = {data.alamat}")
            no += 1


mahasiswa1 = Mahasiswa(
    "John Doe", "21012345", 20, "Teknik Informatika", "Jl. Kampus No. 123"
)
mahasiswa2 = Mahasiswa(
    "Jane Smith", "22023456", 21, "Manajemen Bisnis", "Jl. Maju Mundur No. 456"
)

daftar = DaftarMahasiswa()

daftar.tambah(mahasiswa1)
daftar.tambah(mahasiswa2)

daftar.tampil()

