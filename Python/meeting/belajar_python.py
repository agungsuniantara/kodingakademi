def luas():
    panjang = int(input("panjang = "))
    lebar = int(input("lebar = "))
    return panjang, lebar, panjang * lebar

n = int(input("masukan n = "))
for i in range(n):
    a, b, c = luas()
    print(f"Hasil {i + 1} : ")
    print(f"panjang = {a}")
    print(f"lebar = {b}")
    print(f"luas = {c}")