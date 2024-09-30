data = []

for i in range(5):
    angka = int(input("masukan angka : "))
    data.append(angka)

def hasil(*a):
    tambah = sum(a[0])
    n = len(a[0])
    return tambah, n
    
jumlah, banyak = hasil(data)

rata = lambda a,b : print(a / b)

rata(jumlah, banyak)