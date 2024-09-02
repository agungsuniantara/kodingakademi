class hewan:
    nama = "kucing" # atribut
    kaki = 5 # atribut
    
    def __init__(self, a, b): # konstruktor
        self.ekor = a 
        self.bulu = b
    
    def tampil_nama(self):
        print("nama = ",self.nama)
        
    def tampil_kaki(self):
        print("kaki = ",self.kaki)
    
    def tampil_ekor(self):
        print("ekor = ",self.ekor)
        
    def tampil_bulu(self):
        print("bulu = ",self.bulu)

test = hewan(10,20)
test2 = hewan(100,200)

print(test.nama)
print(test.ekor)
test.tampil_nama()
test.tampil_kaki()
test.tampil_ekor()
test.tampil_bulu()

test2.tampil_ekor()
test2.tampil_bulu()
