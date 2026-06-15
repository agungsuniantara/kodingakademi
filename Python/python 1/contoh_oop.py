class mobil:
    roda = 4
    pintu = 4
    
    def __init__(self, a, b): # constructor
        self.merk = a
        self.harga = b
    
    def maju(self):
        print(f"Mobil {self.merk} maju")
    
    def mundur(self):
        print(f"Mobil {self.merk} mundur")

avanza = mobil("Avanza", 20000000)
xenia = mobil("Xenia", 25000000)

print(avanza.roda)
print(xenia.pintu)
print(avanza.merk)
print(xenia.harga)

avanza.maju()
xenia.mundur()