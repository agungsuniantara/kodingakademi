
# Algoritma O(1) (Konstan)
def constant_algo(items):
    result = items[0] * items[0]
    return result

items = [1, 2, 3, 4, 5]
print(constant_algo(items))

# Algoritma O(n) (Linier)
def linear_algo(items):
    total = 0
    for item in items:
        total += item
    return total

items = [1, 2, 3, 4, 5]
print(linear_algo(items))

# Algoritma O(n^2) (Kuadratik)
def quadratic_algo(items):
    result = []
    for i in items:
        for j in items:
            result.append((i, j))
    return result

items = [1, 2, 3, 4]
print(quadratic_algo(items))

# Algoritma O(log n) (Logaritmik)
def logarithmic_algo(n):
    result = []
    while n > 1:
        result.append(n)
        n = n // 2
    return result

print(logarithmic_algo(16))

# Algoritma O(1) (Konstan): Banyak outputnya tidak tergantung pada ukuran input. Algoritma konstan memiliki waktu eksekusi yang tetap, tidak peduli seberapa besar inputnya.

# Algoritma O(n) (Linier): Banyak outputnya sebanding dengan ukuran inputnya. Artinya, semakin besar inputnya, semakin banyak operasi yang diperlukan, dan waktu eksekusi algoritma tumbuh secara linier sesuai dengan pertumbuhan ukuran input.

# Algoritma O(n^2) (Kuadratik): Banyak outputnya dapat berkembang secara kuadratik dengan pertumbuhan inputnya. Ini berarti bahwa setiap tambahan unit dalam input dapat menyebabkan penambahan operasi sebanyak kuadrat dari input tersebut.

# Algoritma O(log n) (Logaritmik): Banyak outputnya tidak berkembang secara linier dengan pertumbuhan inputnya. Algoritma dengan kompleksitas logaritmik memperkecil masalah secara eksponensial dengan setiap iterasi, sehingga waktu eksekusi cenderung tetap efisien bahkan dengan pertumbuhan input yang besar. Jumlah operasi dalam algoritma logaritmik tumbuh secara logaritmik terhadap ukuran inputnya.

# kecepatan : 

# 1. Konstan (O(1)): Algoritma konstan memiliki waktu eksekusi yang tetap, tidak peduli seberapa besar inputnya. Ini adalah yang paling cepat dari semua kompleksitas waktu karena waktu eksekusinya tidak terpengaruh oleh ukuran input.

# 2. Logaritmik (O(log n)): Algoritma logaritmik memperkecil masalah secara eksponensial dengan setiap iterasi, sehingga waktu eksekusinya cenderung tetap efisien bahkan dengan pertumbuhan input yang besar. Meskipun tidak secepat algoritma konstan, algoritma logaritmik masih dianggap sangat cepat karena waktu eksekusinya tumbuh secara logaritmik terhadap ukuran input.

# 3. Linier (O(n)): Algoritma linier memiliki waktu eksekusi yang sebanding dengan ukuran inputnya. Semakin besar inputnya, semakin banyak operasi yang diperlukan, dan waktu eksekusi algoritma tumbuh secara linier sesuai dengan pertumbuhan ukuran input.

# 4. Kuadratik (O(n^2)): Algoritma kuadratik memiliki waktu eksekusi yang berkembang secara kuadratik dengan pertumbuhan inputnya. Ini berarti bahwa setiap tambahan unit dalam input dapat menyebabkan penambahan operasi sebanyak kuadrat dari input tersebut. Algoritma kuadratik biasanya lebih lambat daripada algoritma linier dan logaritmik, terutama untuk input yang besar.

