# looping = perulangan

print("halo")
print("halo")

# for loops = perulangan yang digunakan jika sudah mengetahui kapan berakhirnya.

print("looping pertama : ")

for i in range(2): # (stop)
    print(i)
    print("halo")
    
print("looping kedua : ")

for i in range(1, 5): # (start, stop)
    print(i)
    
print("looping ketiga : ")

for i in range(0, 6, 2): # (start, stop, step)
    print(i)

print("looping keempat : ")

items = ["apple", "orange", "banana"]

for i in items:
    print(i)
    
print("looping kelima : ")

angka = [1, 2, 3, 4, 5]

for i in angka:
    if i % 2 == 0:
        print(f"angka {i} = genap")
    else:
        print(f"angka {i} = ganjil")
        
# while loops = perulangan yang digunakan jika tidak diketahui kapan berakhirnya.
# while loops = perulangan jika kondisinya benar maka akan terus berulang.

print("looping keenam (while) : ")

i = 1

while i < 5:
    print(i)
    i += 1
    
print("looping ketujuh (while) : ")

while True:
    user = input("masukan kata (yes / no) : ")
    if user == "no":
        break
    
# nested looping

for i in range(3):
    for z in range(3):
        print("* ", end = "")
    print("")





