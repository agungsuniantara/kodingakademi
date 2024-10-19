angka = int(input("masukan angka : "))

if angka >= 0 & angka <= 50:
    print("nilai D")
elif angka >= 51 & angka <= 70:
    print("nilai C")
elif angka >= 71 & angka <= 80:
    print("nilai B")
elif angka >= 81 & angka <= 100:
    print("nilai A")
else:
    print("nilai tidak sesuai")

# no 2

if angka % 2 != 0:
    print("angka ganjil")
else:
    print("angka genap")


score = 0 # 1 # 10
end_score = 10

while(score <= end_score):
    print(f"skor = {score}")
    score += 1

print("permainan selesai")

