if True:
    print("kondisi if 1 benar") 
elif True:
    print("kondisi elif benar 1")
elif False:
    print("kondisi elif benar 2")
else:
    print("kondisi if salah")

username = "bambang"

# if indentasi
if username == "admin": 
    print("halo admin")
elif username == "user": 
    print("halo user")
else:
    print("bukan admin / user")

username = "bambang"
password = 123

if username == "admin" and password == 123: 
    print("halo admin")
elif username == "user" and password == 123: 
    print("halo user")
elif username == "user" or password == 123:
    print("silahkan coba dulu")
else:
    print("bukan admin / user")

# if inline
nama = "agung"
if nama == "agung" : print(f"halo {nama}")

# nested if
username = "bambang"
nama = "wahyu"

if username == "bambang": # true
    if nama == "wahyu": # true
        print("akun sesuai")
    else :
        print("akun tidak sesuai")
else : 
    print("username tidak sesuai")

# ternary
username = "admin"
hasil = "username benar" if username == "admin" else "username salah"
print(hasil)

# match (switch case)
hari = input("masukan hari : ")
match hari:
    case "senin":
        print("hari kerja")
    case "selasa":
        print("hari kerja")
    case "rabu":
        print("hari kerja")
    case "kamis":
        print("hari kerja")
    case "jumat":
        print("hari kerja")
    case "sabtu":
        print("hari libur")
    case "minggu":
        print("hari libur")
    case _:
        print("hari tidak valid")

# conditional if : menggunakan boolean (true / false) sebagai acuan
# match : menggunakan nilai value sebagai acuan.