class Word:
    def __init__(self):
        self.nama = []
    
    def masuk(self, nama):
        self.nama.append(nama)
    
    def filter(self):
        vowels = ['a', 'i', 'u', 'e', 'o']
        filtered_name = []

        for i in self.nama:
            if not any(vowel in i.lower() for vowel in vowels):
                filtered_name.append(i)

        return filtered_name

if __name__ == '__main__':
    data = Word()
    
    while True:
        contoh = input("masukan nama : ")
        data.masuk(contoh)
        ask = input("masih ingin menambah ? ")
        if ask.lower() == "tidak":
            break
    
    hasil = data.filter()
    print(hasil)
