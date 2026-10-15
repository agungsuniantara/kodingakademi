# operator logika

angka1 = 10
angka2 = 20
angka3 = 30

# and (&&) = jika salah satu kondisi false maka hasilnya false
# or (||) = jika salah satu kondisi true maka hasilnya true
# not (negasi) = kebalikan

print(angka1 > angka2 and angka3 > angka2) # false and true = false
print(angka1 > angka2 or angka3 > angka2) # false or true = true
print(not(angka1 > angka2) and angka3 > angka2) # true and true = true

# conditional statement (if, elif, else)

if True:
    print("if pertama")
elif True:
    print("if kedua")
else:
    print("ini else")
    
username = input("masukan nama : ")
password = input("masukan password : ")

print(username == "admin" and password == "123")

if username == "admin" and password == "123":
    print("halo admin")
elif username == "user" and password == "9090":
    print("halo user")
elif username == "manager" and password == "2222":
    print("halo manager")
else:
    print("user tidak dikenali")
    
