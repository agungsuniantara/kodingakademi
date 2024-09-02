menu = ["1. Nasi Goreng", "2. Mie Goreng", "3. Es Jeruk", "4. Jus Mangga", "5. Pisang Goreng"]
pesanan = []

print("Silahkan Pilih Menu Makanan")
for i in menu:
    print(i)

jawaban = input("Silahkan Ketikan Menu Yang Akan Dipesan = ")
pesanan.append(jawaban)
tanya = input("Masih ingin memesan ? ")
while(tanya == "iya"):
    jawaban = input("Silahkan Ketikan Menu Yang Akan Dipesan = ")
    pesanan.append(jawaban)
    tanya = input("Masih ingin memesan ? ")
    if tanya == "tidak":
        break

print("Menu Pesanan Anda = ")
for j in pesanan:
    print(j)

harga = len(pesanan) * 20000
print("Total Harga =",harga)
    
