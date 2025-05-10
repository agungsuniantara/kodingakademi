# soal if 

nilai = int(input("Masukkan nilai:"))
if nilai >= 0 and nilai <= 50:
    print("Nilai : D")
elif nilai >= 51 and nilai <= 70:
    print("Nilai: C")
elif nilai >= 71 and nilai <= 80:
    print("Nialai: B")
elif nilai >= 81 and nilai <= 100:
    print("Nialai: A")
else:
    print("Format nilai salah")

# no 1

for i in range(1,11):
    print(i)
    
# no 2

kolom = 5
baris = 5

for i in range(baris): # i = 1
    for z in range(kolom): # z = 1
        if z <= i : 
            print("*", end=" ")
    print(" ")

# no 4 

n = int(input("masukan angka n : "))
jumlah = 0
for i in range(n + 1): # i = 0
    if i % 2 == 0:
        jumlah += i

print(f"jumlah angka genap sampai n : {jumlah}")

# no 5

total = 0
z = 0

for i in range(5):
    angka = float(input("masukan angka : "))
    total += angka
    z += 1

rata = total / z
print(f"Hitung rata - rata : {rata}")
    