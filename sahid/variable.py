nama = "sahid" # string
alamat = "denpasar" # string 
umur = 40 # integer (int)
angka = 10.5 # float 
benar = True # boolean 
salah = False # boolean

print(f"nama : {nama}")
print("alamat : ", alamat)
print("umur : ", umur)
print("angka : ", angka)
print("benar : ", benar)
print("salah : ", salah)

print("tipe data angka : ", type(angka))

# konversi angka 

ubah = int(angka)

print("angka ke int : ", ubah)
print("tipe data : ", type(ubah))

if nama == "sahid":
    print("halo sahid")