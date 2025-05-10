# for loop

for i in range(3): # range(batas)
    print(f"{i} - hallo")

print("\n")

for i in range(1,4): # range(awal, batas)
    print(f"{i} - hallo")

print("\n")

for i in range(0,6,2): # range(awal, batas, langkah)
    print(f"{i} - hallo")
    
# for loop list 

print("\n")

data = ["a", "b", "c", "d"]

for index, value in enumerate(data):
    print(f"{index} - {value}")

print("\n")

for i in data:
    print(i)
    
# for loop string

print("\n")

word = "hallo"

for i in word:
    print(i)
    
# while loop

print("\n")

angka = 0 
while angka < 5:
    print("hello")
    angka += 1 
    
# while loop continue

print("\n")

angka = 0 
while angka < 5: 
    angka += 1
    if angka == 3: 
        continue
    print(f"angka sekarang = {angka}")

# while loop break

print("\n")

angka = 0 
while angka < 5:
    angka += 1
    if angka == 3: 
        break
    print(f"angka sekarang = {angka}")

# nested looping

print("\n")

for i in range(2): 
    for z in range(3): 
        print(f"{i} {z}")

# loop else

print("\n")

for i in range(3):
    print(i)
else:
    print("selesai !!!")
    
# loop zip

print("\n")

nama = ["gadis", "agung", "wahyu"]
umur = [17, 26, 30]

for name, age in zip(nama, umur):
    print(f"{name} - {age} tahun")
    
# loop sorted

print("\n")

number = {3,1,2,5,6}

for i in sorted(number):
    print(i)
    
# loop pass

print("\n")

buah = ["pisang", "apple"]

for i in buah:
    pass
    
