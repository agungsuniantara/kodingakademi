positive = []
negative = []
angka = []

print("masukkan 10 buah angka");
for i in range(10):
    angka[i] = int(input("masukan angka : "))

for x in angka:
    if x > 0:
        positive.append(x)
    else:
        negative.append(x)

print("bilangan positive : ", positive)
print("bilangan negative : ", negative)