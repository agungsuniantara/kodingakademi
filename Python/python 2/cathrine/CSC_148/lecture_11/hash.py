class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Membuat array kosong dengan ukuran yang telah ditentukan

    def _hash_function(self, key):
        return hash(key) % self.size  # Fungsi hash sederhana, menggunakan fungsi hash bawaan Python

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Jika kunci sudah ada, perbarui nilai yang sesuai
                return
        self.table[index].append([key, value])  # Jika kunci belum ada, tambahkan pasangan kunci-nilai baru

    def get(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # Jika kunci ditemukan, kembalikan nilai yang sesuai
        return None  # Jika kunci tidak ditemukan, kembalikan None

# Contoh penggunaan:
hash_table = HashTable(10)  # Membuat hash table dengan ukuran 10
hash_table.insert('apple', 5)
hash_table.insert('banana', 7)
hash_table.insert('orange', 3)

print(hash_table.get('apple'))  # Output: 5
print(hash_table.get('banana'))  # Output: 7
print(hash_table.get('orange'))  # Output: 3
print(hash_table.get('grape'))  # Output: None (kunci tidak ditemukan)
