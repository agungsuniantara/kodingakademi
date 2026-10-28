# class = blueprint

class mobil:
    roda = 4
    pintu = 4
    
    def __init__(self, a, b):
        self.nama = a
        self.harga = b
    
    def maju(self):
        print("mobil maju")
    
    def mundur(self):
        print("mobil mundur")
    
    def berhenti(self):
        print("mobil berhenti")
    
agya = mobil("agya", 10000000)
avansa = mobil("avansa", 50000000)
pajero = mobil("pajero", 100000000)

print(agya.roda)
print(avansa.roda)
agya.maju()

print("harga agya = ", agya.harga)
print("harga avansa = ", avansa.harga)






    
    