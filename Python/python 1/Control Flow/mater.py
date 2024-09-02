# if statements

username = "admin"
if username == "admin":
     print("Selamat Datang Admin!")

username2 = "user"
if username2 == "admin":
     print("Selamat Datang user!")

print()

nilai = int(input("Masukan Nilai Ujian = "))
if(nilai > 60):
     print("Selamat Anda Lulus Ujian!")
else:
     print("Maaf Anda Harus Mengulang Tahun Depan")

print()

username = input("Masukan Username Anda = ")
if(username == "admin"):
    print("Salamat Datang Admin!")
elif(username == "robert"):
    print("Selamat Datang Robert di Koding Akademi!")
else:
    print("Maaf Anda Tidak Terdaftar Sebagai Pengguna")

print()

username = input("Masukan Username Anda = ")
password = input("Masukan Password Anda = ")
if(username == "admin" and password=="123"):
     print("Selamat Datang di Koding Akademi!")
else:
     print("Username dan atau Password salah!")


