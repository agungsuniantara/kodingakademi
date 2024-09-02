class hewan:
    def __init__(self, nama, umur, jenis):
        self.nama = nama
        self.umur = umur
        self.jenis = jenis

    def tampil_kucing(self):
        print(f"kucing {self.nama}, umur {self.umur}, jenis {self.jenis} lagi makan")

    def tampil_anjing(self):
        print(f"anjing {self.nama}, umur {self.umur}, jenis {self.jenis} lagi makan")


class kucing(hewan):
    def __init__(self, nama, umur, jenis, tahun):
        super().__init__(nama, umur, jenis)
        self.year = tahun

    def tampil_data(self):
        print(f"{self.nama}, {self.umur}, {self.jenis}, {self.year}")


class anjing(hewan):
    pass


yudis = anjing("yudis", 20, "husky")
wahyu = kucing("wahyu", 30, "anggora", 2022)

yudis.tampil_anjing()
wahyu.tampil_data()
