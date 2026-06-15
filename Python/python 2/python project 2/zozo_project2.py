class karyawan:
    def __init__(self):
        self.data = {}
    
    def tambah_data(self, nama, status, tahun, gaji):
        self.data[nama] = [status, tahun, gaji]

    def edit_data(self, nama):
        for key, value in self.data.items():
            if nama == key:
                while True:
                    pilih = input("ketik data yang ingin dirubah :")
                    if pilih == "status":
                        new_status = input("Masukkan status baru: ")
                        value[0] = new_status
                    elif pilih == "tahun":
                        new_tahun = input("Masukkan tahun baru: ")
                        value[1] = new_tahun
                    elif pilih == "gaji":
                        new_gaji = input("Masukkan gaji baru: ")
                        value[2] = new_gaji
                    else:
                        print("Data tidak ada / tidak boleh dirubah.")
                    
                    another = input("Apakah Anda ingin mengubah data lain untuk karyawan ini? (y/n): ")
                    if another.lower() != 'y':
                        break
                break
            else:
                print("Data tidak ditemukan.")
    
    def hapus_data(self, nama):
        if nama in self.data:
            del self.data[nama]
            print("Data karyawan berhasil dihapus.")
        else:
            print("Data tidak ditemukan.")

    def tampil_data(self):
        print("+----------------------------------+")
        print("| Nama Pegawai | Status | Tahun Masuk | Gaji |")
        for key, value in self.data.items():
            print(f"| {key:<12} | {value[0]:<6} | {value[1]:<11} | {value[2]:<6} |")
        print("+----------------------------------+")

database = karyawan() 

while True:
    print("Selamat datang di sistem manajemen karyawan")
    print("silahkan memilih menu yang tersedia :")
    print("1. Tambah Data Karyawan")
    print("2. Edit Data Karyawan")
    print("3. Hapus Data Karyawan")
    print("4. Tampilkan Data Karyawan")
    print("5. Keluar")
    choice = input("Masukkan pilihan Anda (1-5): ")
    
    if choice == '1':
        nama = input("Masukkan nama karyawan: ")
        status = input("Masukkan status karyawan (Tetap/Kontrak): ")
        tahun = input("Masukkan tahun masuk karyawan: ")
        gaji = input("Masukkan gaji karyawan: ")
        database.tambah_data(nama, status, tahun, gaji)
        print("Data karyawan berhasil ditambahkan.")
    elif choice == '2':
        nama_edit = input("Masukkan nama karyawan yang datanya ingin diubah: ")
        database.edit_data(nama_edit)
    elif choice == '3':
        nama_hapus = input("Masukkan nama karyawan yang datanya ingin dihapus: ")
        database.hapus_data(nama_hapus)
    elif choice == '4':
        database.tampil_data()
    elif choice == '5':
        print("Terima kasih telah menggunakan sistem manajemen karyawan.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
    
    
    
