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
    pass


class anjing(hewan):
    pass


wahyu = kucing("wahyu", 20, "anggora")
yudis = kucing("yudis", 20, "husky")

wahyu.tampil_kucing()
yudis.tampil_anjing()
