class manusia:
    def __init__(self, a, b, c):
        self.nama = a 
        self.umur = b 
        self.alamat = c 
    
    def tampil_nama(self):
        print("nama : ", self.nama)
        
    def tampil_umur(self):
        print("umur : ", self.umur)

jilian = manusia("jilian", "12 tahun", "denpasar")
jilian.tampil_nama()