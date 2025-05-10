class Buku:
    def __init__(self, judul, penulis, harga):
        self.judul = judul
        self.penulis = penulis
        self.harga = harga

    def __str__(self):
        return f"{self.judul} - {self.penulis} - Rp {self.harga}"
    
class TokoBuku:
    def __init__(self):
        self.daftar_buku= []
    
    def tambah_buku(self):
        judul = input("Masukkan judul buku:")
        penulis = input("Masukkan nama penulis:")
        try:
            harga = int(input("Masukkan harga buku:"))
            if harga <= 0:
                print("[!] Input yang dimasukkan tidak valis [!]")
                return
            buku = Buku(judul, penulis, harga)
            self.daftar_buku.append(buku)
            print(f"[+] Buku berjudul {judul} dengan penulis {penulis} ditambahkan ke daftar buku [+]")
        except ValueError:
            print("[!] Input harga harus berupa angka [!]")
    
    def tampil_buku(self):
        print("=" * 40)
        print(f"\t\tDaftar Buku")
        print("=" * 40)

        if not self.daftar_buku:
            print("Belum ada buku di daftar:")
        else:
            for idx, buku in enumerate(self.daftar_buku, start=1):
                print(f"{idx}.{buku}")
        print()
    
    def hitung_total(self):
        judul_cari = input("Masukkan judul buku:")
        try:
            jumlah = int(input("Masukkan jumlahnya:"))
            ketemu = False

            for buku in self.daftar_buku:
                if buku.judul == judul_cari:
                    total = buku.harga * jumlah
                    print(f"Total harga belanjaan adalah Rp {total}.00")
                    ketemu = True
                    break
            
            if not ketemu:
                print(f"Buku berjudul {judul_cari} tidak tersedia di toko.")
        except ValueError:
            print("[!] Input jumlah harus berupa angka [!]")
    
    def menu(self):
        while True:
            print("=" * 40)
            print(f"\t\tToko Buku")
            print("=" * 40)
            print("1. Tambah Buku")
            print("2. Tampilkan Daftar Buku")
            print("3. Hitung total Harga Belanja")
            print("0. Keluar")
            pilih = input("Pilih menu:")

            if pilih == '1':
                self.tambah_buku()
            elif pilih == '2':
                self.tampil_buku()
            elif pilih == '3':
                self.hitung_total()
            elif pilih == '0':
                print(f"Keluar dari program.")
                break
            else:
                print(f"Menu tidak valid!")

if __name__ == "__main__":
    toko = TokoBuku()
    toko.menu()