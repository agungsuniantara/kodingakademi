class mahasiswa:
    def __init__(self):
        self.data = {}
    
    def tambah_data(self, nim, nama, usia, jurusan, alamat):
        self.data[nim] = [nama, usia, jurusan, alamat]
    
    def edit_data(self, nama):
        for key, value in self.data.items():
            if nama in value:
                pilih = input("ketik data yang ingin dirubah : ")
                if pilih == "nama":
                    value[0] = input("masukan nama baru : ")
                elif pilih == "usia":
                    value[1] = input("masukan usia baru : ")
                elif pilih == "jurusan":
                    value[2] = input("masukan jurusan baru : ")
                elif pilih == "alamat":
                    value[3] = input("masukan alamat baru : ")
                else:
                    print("data tidak ada / tidak boleh dirubah")
            else:
                print("data tidak tersedia")
                
    def tampil_data(self):
        print("Berikut data mahasiswa :")
        for key, value in self.data.items():
            print("Nama mahasiswa : ", value[0])
            print("NIM mahasiswa : ", key)
            print(f"Tahun masuk : 20{key[0:2]}") # 178888

data = mahasiswa()

data.tambah_data("17888999", "lorenzo", "17 tahun", "informatika", "denpasar")
data.tambah_data("163232", "wahyu", "17 tahun", "informatika", "denpasar")
data.tampil_data()
            