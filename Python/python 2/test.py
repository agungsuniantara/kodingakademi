a = ["caku", "baku", "aku"] # [caku, baku]
baru = [] # [aku, baku]

for i in range(len(a)):
    terkecil = min(a)
    baru.append(terkecil)
    a.remove(terkecil)

print(baru)


