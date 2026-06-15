class mahasiswa:
    def __init__(self):
        self.data = {}
    
    def tambah_data(self, nim, nama, usia, jurusan, alamat):
        self.data[nim] = [nama, usia, jurusan, alamat]

    def edit_data(self, nama):
        for key, value in self.data.items():
            if nama in value:
                pilih = input("ketik data yang ingin dirubah :")
                if pilih == "nama":
                    new_nama = input("Masukkan nama baru: ")
                    value[0] = new_nama
                elif pilih == "usia":
                    new_usia = input("Masukkan usia baru: ")
                    value[1] = new_usia
                elif pilih == "jurusan":
                    new_jurusan = input("Masukkan jurusan baru: ")
                    value[2] = new_jurusan
                elif pilih == "alamat":
                    new_alamat = input("Masukkan alamat baru: ")
                    value[3] = new_alamat
                else:
                    print("Data tidak ada / tidak boleh dirubah.")
            else:
                print("Data tidak ditemukan.")

    def tampil_data(self):
        print("Berikut data mahasiswa:")
        for key, value in self.data.items():
            print("Nama:", value[0])
            print("NIM:", key)
            print(f"Tahun masuk : 20{key[0:2]}")
            print("Usia:", value[1])
            print("Jurusan:", value[2])
            print("Alamat:", value[3])
            print("Terimakasih Sudah Menggunakan Sistem Ini")

data = mahasiswa()

data.tambah_data("22060120120045", "Lorenzo", 17, "Cyber Secutiry", "Denpasar")
data.tampil_data()

nama_edit = input("Masukkan nama yang datanya ingin diubah: ")
data.edit_data(nama_edit)