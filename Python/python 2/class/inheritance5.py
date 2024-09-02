class perpustakaan:
    def __init__(self, nama_buku, jumlah_buku):
        self.nama = nama_buku
        self.jumlah = jumlah_buku
    
    def nama_buku(self):
        print(self.nama)
    
    def tampil_jumlah(self):
        print(self.jumlah)

class mahasiswa(perpustakaan):
    def __init__(self, nama_buku, jumlah_buku, nama_mahasiswa):
        super().__init__(nama_buku, jumlah_buku)
        self.nama_mhs = nama_mahasiswa

    def nama_mahasiswa(self):
        print(self.nama_mhs)
        
order1 = perpustakaan("avanger", 20)
order1.nama_buku()

order2 = mahasiswa("perahu", 10, "mang agus")
order2.nama_buku()
order2.nama_mahasiswa()
