class hewan:
    def __init__(self, a, b):
        self.name = a 
        self.breed = b
    
    def makan(self):
        print(self.nama + " lagi makan")
    
cihua = hewan("wayan", "cihuahua")
cihua.makan()

data2 = hewan("agus", "bulldog")
data2.makan()