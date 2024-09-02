# min

data= [6, 7, 2, 3, 5]
print("Nilai terkecilnya adalah", min(data))

data = [1, 4, 1, 6, 5]
data2 = [8, 2, 1, 8]
print("Iterable terkecilnya adalah", min(data, data2))

data = [1, 4, 1, 6, 5]
data2 = [8, 2, 1, 8]
print("Iterable terkecil berdasarkan jumlah anggotanya adalah", min(data, data2, key=len))

print("Huruf terkecilnya adalah", min("python"))
print("Nilai terkecilnya adalah", min(5, -7))
print("Nilai terkecilnya adalah", min(-5, -7, 0, -1))