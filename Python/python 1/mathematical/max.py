# max

data= [6, 7, 2, 3, 5]
print("Nilai terbesarnya adalah", max(data))

data = [11, 1, 1, 1, 12]
data2 = [10, 1, 1, 13]
print("Iterable terbesarnya adalah", max(data, data2))

data = [1, 4, 1, 6, 5]
data2 = [8, 2, 1, 8,10,11]
print("Iterable terbesar berdasarkan jumlah anggotanya adalah", max(data, data2, key=len))

print("Huruf terbesarnya adalah", max("Python"))
print("Nilai terbesarnya adalah", max(5, 7))
print("Nilai terbesarnya adalah", max(-5, -7))