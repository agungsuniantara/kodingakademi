data = {
    "1" : "apel",
    "2" : "mangga",
    "3" : "anggur"
}

for i in data:
    angka = int(i)
    if angka % 2 != 0:
        data[i] = "hewan"

print(data)

user = input("tuliskan teks : ")

a = 0
i = 0
u = 0
e = 0
o = 0

for i in user:
    if i == "a":
        a += 1