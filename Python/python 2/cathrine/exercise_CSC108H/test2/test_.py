import unittest
from vowel import Word

class TestVowel(unittest.TestCase):
    def test_data(self):
        name = Word()
        data_test = []

        while True:
            contoh = input("masukan nama : ")
            data_test.append(contoh)
            name.masuk(contoh)
            ask = input("masih ingin menambah ? ")
            if ask.lower() == "tidak":
                break

        self.assertEqual(name.nama, data_test)
    
    def test_vowel(self):
        name = Word()
        hasil = name.filter()
        
        self.assertEqual(name.filter(), hasil)
        
if __name__ == '__main__':
    unittest.main()
