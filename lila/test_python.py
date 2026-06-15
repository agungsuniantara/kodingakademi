class mobil:
    def __init__(self, a, b, c, d):
        self.nama = a
        self.roda = b
        self.warna = c
        self.tahun = d

    def jalan(self):
        print("Mobil berjalan")
    def berhenti(self):
        print("Mobil berhenti")

class pemilik (mobil):
    def __init__(self, a, b, c, d, e):
        super().__init__(a, b, c, d)
        self.nama_pemilik = e

    def info_pemilik(self):
        print("Nama Pemilik:", self.nama_pemilik)
        
mobil1 = mobil("Agya", 4, "Merah", 2020)
mobil1.jalan()
mobil1.berhenti()

pemilik1 = pemilik("Avanza", 4, "Hitam", 2019, "Budi")
pemilik1.info_pemilik()
pemilik1.jalan()
pemilik1.berhenti()