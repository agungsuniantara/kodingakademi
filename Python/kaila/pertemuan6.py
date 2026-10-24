# function adalah blueprint yang dapat digunakan berulang kali
# function (void, parameter, return, recursion)

# function void = fungsi yang tidak mengembalikan nilai
# function void bisa menggunakan parameter dan tanpa parameter

def persegi_panjang(a, b): # -> function void
    luas = a * b
    print(f"luas persegi panjang = {luas}")
    
persegi_panjang(10, 5)

total = 0 # variabel local

def tambah():
    global total # global = memberikan function akses untuk mengubah variabel local
    total += 1
    print(total)
    
tambah()
    





