class pegawai:
    def __init__(self):
        self.data = {} # key : value
        
    def tambah_pegawai(self, nama, status, tahun, gaji):
        self.data[nama] = [status, tahun, gaji]
    
    def tampilkan_pegawai(self):
        for nama, info in self.data.items():
            print(f"Nama: {nama}, Status: {info[0]}, Tahun: {info[1]}, Gaji: {info[2]}")
    
    def hapus_pegawai(self, nama):
        if nama in self.data:
            del self.data[nama]
        else:
            print("Pegawai tidak ditemukan.")
    
    def edit_pegawai(self, nama):
        if nama in self.data:
            status = input("Masukkan status baru (kosongkan jika tidak diubah): ")
            tahun = input("Masukkan tahun baru (kosongkan jika tidak diubah): ")
            gaji = input("Masukkan gaji baru (kosongkan jika tidak diubah): ")
            if status:
                self.data[nama][0] = status
            if tahun:
                self.data[nama][1] = tahun
            if gaji:
                self.data[nama][2] = gaji
        else:
            print("Pegawai tidak ditemukan.")

data = pegawai()

while True:
    print("1. Tambah Pegawai")
    print("2. Tampilkan Pegawai")
    print("3. Edit Pegawai")
    print("4. Hapus Pegawai")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == '1':
        nama = input("Masukkan nama pegawai: ")
        status = input("Masukkan status pegawai: ")
        tahun = input("Masukkan tahun bergabung: ")
        gaji = input("Masukkan gaji pegawai: ")
        data.tambah_pegawai(nama, status, tahun, gaji)
    elif pilihan == '2':
        data.tampilkan_pegawai()
    elif pilihan == '3':
        nama = input("Masukkan nama pegawai yang ingin diedit: ")
        data.edit_pegawai(nama)
    elif pilihan == '4':
        nama = input("Masukkan nama pegawai yang ingin dihapus: ")
        data.hapus_pegawai(nama)
    elif pilihan == '5':
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")


number = 0 
print(number)
number += 1
print(number)
number += 1
print(number)
number += 1
print(number)
number += 1
print(number)
number -= 1