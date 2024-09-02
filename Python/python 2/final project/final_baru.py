class Karyawan:
    def __init__(self, nama, status, tahun, gaji):
        self.nama = nama
        self.status = status
        self.tahun = tahun
        self.gaji = gaji

class Data:
    def __init__(self):
        self.dict = {}

    def tambah(self, karyawan):
        nama = karyawan.nama
        self.dict[nama] = karyawan

    def edit(self, cari, data_baru):
        for nama, data in self.dict.items():
            if nama == cari:
                data.status = data_baru["status"]
                data.tahun = data_baru["tahun"]
                data.gaji = data_baru["gaji"]

    def hapus(self, cari):
        hapus = []
        for nama in self.dict:
            if nama == cari:
                hapus.append(nama)

        for i in hapus:
            self.dict.pop(i)

    def tampil(self):
        print("daftar karyawan : ")
        no = 1
        for nama, data in self.dict.items():
            print(f"data {no}")
            print(f"nama : {nama}")
            print(f"status = {data.status}")
            print(f"tahun = {data.tahun}")
            print(f"gaji = {data.gaji}")
            no += 1

def menu():
    print("Selamat datang di sistem informasi pegawai")
    print("Silahkan memilih menu : ")
    print("1. Tambah pegawai")
    print("2. Edit pegawai")
    print("3. Hapus pegawai")
    print("4. Tampilkan pegawai")
    print("5. keluar")


data = Data()

while True:
    menu()

    pilih = int(input("pilih menu : "))

    if pilih == 1:
        masuk = int(input("tambah berapa data : "))
        no = 1
        for i in range(masuk):
            print(f"data {no}")
            nama = input("masukan nama : ")
            status = input("masukan status : ")
            tahun = int(input("masukan tahun : "))
            gaji = int(input("masukan gaji : "))

            data.tambah(Karyawan(nama, status, tahun, gaji))
            no += 1

    elif pilih == 2:
        data.tampil()

        nama = input("pilih nama : ")
        status = input("masukan status : ")
        tahun = int(input("masukan tahun : "))
        gaji = int(input("masukan gaji : "))

        data_baru = {"nama": nama, "status": status, "tahun": tahun, "gaji": gaji}
        data.edit(nama, data_baru)

    elif pilih == 3:
        data.tampil()
        nama = input("masukan data nama yang ingin dihapus :")
        data.hapus(nama)

    elif pilih == 4:
        data.tampil()

    elif pilih == 5:
        break
