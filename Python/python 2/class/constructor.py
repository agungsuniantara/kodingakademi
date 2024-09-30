class dog:
    def __init__(self, a, b, c, d):
        self.breed = a
        self.size = b
        self.age = c
        self.color = d
    
    def eat(self):
        print(f"{self.breed} lagi makan")
    def sleep(self):
        print(f"{self.nama} lagi tidur")
    def tampil(self):
        print(f"Nama = {self.breed}, size = {self.size}")

anjing1 = dog("mastiff", 20, 10, "red")
anjing1.eat()
anjing1.tampil()