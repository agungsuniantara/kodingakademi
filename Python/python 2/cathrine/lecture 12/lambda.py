a = 0

def tambah(b):
    global a
    a += b
    print(a)
    
contoh = lambda x: tambah(x)

for i in range(5):
    angka = int(input("masukan angka : "))
    contoh(angka)