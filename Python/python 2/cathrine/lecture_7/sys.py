data1 = open("cathrine\lecture_7\pukul.txt", "r")
data2 = open("cathrine\lecture_7\mesra.txt", "r")

data_action = []
data_romance = []

for i in data1:
    data_action = i.split()

for i in data2:
    data_romance = i.split()

data = {
    "action" : data_action,
    "romance" : data_romance
}

def menu():
    print(data)
    print("pilih aksi berikut ini : ")
    print("1. tambah")
    print("2. edit")
    print("3. hapus")

while True : 
    menu()
    masuk = int(input("masukan aksi : "))
    if masuk == 1:
        print("jenis buku : ")
        for i in data.keys():
            print(i)
        jenis = input("masukan jenis buku : ")
        for a,b in data.items():
            if jenis == a:
                tambah = input("masukan buku baru : ")
                b.append(tambah)
    elif masuk == 2:
        print("jenis buku : ")
        for i in data.keys():
            print(i)
        jenis = input("masukan jenis buku : ")
        for a,b in data.items():
            if jenis == a:
                print(f"buku : {b}")
                edit = input("buku yang mau di edit : ")
                for i in range(len(b)):
                    if edit == b[i]:
                        edit_buku = input("masukan buku baru : ")
                        b[i] = edit_buku
    elif masuk == 3:
        print("jenis buku : ")
        for i in data.keys():
            print(i)
        jenis = input("masukan jenis buku : ")
        for a,b in data.items():
            if jenis == a:
                print(f"buku : {b}")
                edit = input("buku yang mau di edit : ")
                for i in range(len(b)):
                    if edit == b[i]:
                        b.pop(i)
    else:
        break

