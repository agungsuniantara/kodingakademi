buah = {
    1 : "apel",
    2 : "pisang"
}
sayuran = {
    1 : "kangkung",
    2 : "wortel"
}
daging = {
    1 : "ayam",
    2 : "sapi"
}
obat = {
    1 : "paracetamol",
    2 : "mixagrip"
}

buah_copy = buah.copy()
sayuran_copy = buah.copy()
daging_copy = buah.copy()
obat_copy = buah.copy()

while True:
  try:
    username = input("masukan username : ")
    password = input("masukan password : ")

    if username == "admin" and password == "admin":

        while True:
            print(f"halo {username} silahkan memilih menu dibawah : ")
            print("1. tambah barang")
            print("2. hapus barang")
            print("3. edit barang")

            pilih = int(input("masukan pilihan : "))

            if pilih == 1 :
                print("list barang : ")
                print("1. buah")
                print("2. sayuran")
                print("3. daging")
                print("4. obat")

                barang = int(input("pilih barang : "))

                if barang == 1:
          
                    barang_baru = input("masukan nama buah baru : ")
                    buah.update({len(buah) + 1 : barang_baru})

                elif barang == 2:
          
                    barang_baru = input("masukan nama sayuran baru : ")
                    buah.update({len(buah) + 1 : barang_baru})
        
                elif barang == 3:
          
                    barang_baru = input("masukan nama daging baru : ")
                    buah.update({len(buah) + 1 : barang_baru})
        
                elif barang == 4:
          
                    barang_baru = input("masukan nama obat baru : ")
                    buah.update({len(buah) + 1 : barang_baru})
      
            elif pilih == 2 :

                print("list barang : ")
                print("1. buah")
                print("2. sayuran")
                print("3. daging")
                print("4. obat")

                barang = int(input("pilih barang : "))

                if barang == 1 :
          
                    barang_baru = input("masukan nama buah yang ingin dihapus : ")

                    for key, value in buah_copy.items():
                        if barang_baru in value:
                            hapus = buah.pop(key)
                            print(hapus)
          
                elif barang == 2 :
          
                    barang_baru = input("masukan nama sayuran yang ingin dihapus : ")

                    for key, value in sayuran_copy.items():
                        if barang_baru in value:
                            hapus = sayuran.pop(key)
                            print(hapus)
        
                elif barang == 3 :
          
                    barang_baru = input("masukan nama daging yang ingin dihapus : ")

                    for key, value in daging_copy.items():
                        if barang_baru in value:
                            hapus = daging.pop(key)
                            print(hapus)
          
                        elif barang == 4 :
          
                            barang_baru = input("masukan nama obat yang ingin dihapus : ")

                            for key, value in obat_copy.items():
                                if barang_baru in value:
                                    hapus = obat.pop(key)
                                    print(hapus)
        
            elif pilih == 3:

                print("list barang : ")
                print("1. buah")
                print("2. sayuran")
                print("3. daging")
                print("4. obat")

                barang = int(input("pilih barang : "))

                if barang == 1 :
                    list_buah = []

                    for key, value in buah_copy.items():
                        list_buah.append(value)

                        print("list barang : ")
                        print(list_buah)

                    barang_baru = input("masukan nama buah yang ingin di edit : ")

                    for key, value in buah_copy.items():
                        if barang_baru in value:
                            edit = input("masukan nama buah yang baru : ")
                            buah[key] = edit
                            break
          
                elif barang == 2 :
                    list_sayuran = []

                    for key, value in sayuran_copy.items():
                        list_sayuran.append(value)

                        print("list barang : ")
                        print(list_sayuran)

                        barang_baru = input("masukan nama sayuran yang ingin di edit : ")

                        for key, value in sayuran_copy.items():
                            if barang_baru in value:
                                edit = input("masukan nama sayuran yang baru : ")
                                sayuran[key] = edit
                                break
          
                elif barang == 3 :
                    list_daging = []

                    for key, value in daging_copy.items():
                        list_daging.append(value)

                        print("list barang : ")
                        print(list_daging)

                        barang_baru = input("masukan nama daging yang ingin di edit : ")

                        for key, value in daging_copy.items():
                            if barang_baru in value:
                                edit = input("masukan nama sayuran yang baru : ")
                                daging[key] = edit
                                break
          
                elif barang == 4 :
                    list_obat = []

                    for key, value in obat_copy.items():
                        list_obat.append(value)

                    print("list barang : ")
                    print(list_obat)

                    barang_baru = input("masukan nama obat yang ingin di edit : ")

                    for key, value in obat_copy.items():
                        if barang_baru in value:
                            edit = input("masukan nama obat yang baru : ")
                            obat[key] = edit
                            break

            logout = input("ingin logout ?  ")

            if logout == "ya":
                break
            else:
                print(" ")

    elif username == "user" and password == "user" :

        while True :
            print(f"halo {username} silahkan memilih menu dibawah : ")
            print("1. tambah barang")
            print("2. hapus barang")
            print("3. edit barang")

            pilih = int(input("masukan pilihan : "))
    
    kondisi = input("apakah ingin keluar ? ")
      
    if kondisi == "ya":
        break
    else:
        print(" ")

    except ValueError:
        print("masukan data dengan benar")

print(buah)