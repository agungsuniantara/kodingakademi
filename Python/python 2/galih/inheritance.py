class person:
    def __init__(self, a):
        self.nama = a 
    
    def walk(self):
        print(f"{self.nama} lagi berjalan")

class employee(person):
    def __init__(self, a, b):
        super().__init__(a)
        self.id = b
        
    def work(self):
        print(f"{self.id} lagi bekerja")

orang1 = person("galih")
employee1 = employee("wayan", "292929")

orang1.walk()
employee1.walk()
employee1.work()