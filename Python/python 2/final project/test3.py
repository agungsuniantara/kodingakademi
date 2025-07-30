class pegawai:
    def __init__(self):
        self.data = {}

    def tambah_data(self, nama, status, tahun_masuk, gaji):
        self.data[nama] = [status, tahun_masuk, gaji]

    def edit_data(self, nama):
        for key, value in self.data.items():
            if key == nama:
                status = input("Masukkan Status Kerja Baru: ")
                tahun_masuk = input("Masukkan Tahun Masuk Baru: ")
                gaji = int(input("Masukkan Gaji Pegawai Baru: "))
                value[0] = status
                value[1] = tahun_masuk
                value[2] = gaji

    def tampil_data(self):
        for key, value in self.data.items():
            print("Berikut Data Pegawai:")
            print(f"Nama Pegawai: {key}")
            print(f"Status Kerja: {value[0]}")
            print(f"Tahun Masuk: {value[1]}")
            print(f"Gaji Pegawai: {value[2]}")

    def hapus_data(self, nama):
        if nama in self.data:
            del self.data[nama]
            print(f"Data pegawai {nama} telah dihapus.")
        else:
            print(f"Data pegawai {nama} tidak ditemukan.")

data = pegawai()

while True:
    print("Selamat Datang di Sistem Data Pegawai")
    print("1. Tambah Data Pegawai")
    print("2. Edit Data Pegawai")
    print("3. Hapus Data Pegawai")
    print("4. Tampilkan Data Pegawai")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == '1':
        nama = input("Masukkan Nama Pegawai: ")
        status = input("Masukkan Status Kerja: ")
        tahun_masuk = input("Masukkan Tahun Masuk: ")
        gaji = int(input("Masukkan Gaji Pegawai: "))
        data.tambah_data(nama, status, tahun_masuk, gaji)
    elif pilihan == '2':
        nama = input("Masukkan Nama Pegawai yang ingin diedit: ")
        data.edit_data(nama)
    elif pilihan == '3':
        nama = input("Masukkan Nama Pegawai yang ingin dihapus: ")
        data.hapus_data(nama)
    elif pilihan == '4':
        data.tampil_data()
    elif pilihan == '5':
        print("terima kasih sudah menggunakan sistem ini")
        break
    else:
        print("pilihan tidak tersedia")