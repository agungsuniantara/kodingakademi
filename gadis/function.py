# function void : tidak mengembalikan nilai
# function parameter : dapat menerima value
# function return : dapat mengembalikan nilai
# function recursive : dapat memanggil dirinya sendiri
# function lambda : function 1 baris

angka = 10

def tampil1(): # function void
    print("hello world")

def tampil2(nama, alamat): # function parameter
    print(f"nama saya = {nama}, alamat = {alamat}")

def tampil3(a, b): # function return
    result = a + b 
    return result

def ganti():
    global angka # global : memberikan akses function
    angka = 20
    print(angka)

def nested_function(angka1, angka2, angka3): # nested function
    result = tampil3(angka1, angka2) * angka3
    return result

def rekursif(angka): 
    if angka == 0:
        return 10
    else:
        return angka * rekursif(angka - 1)



tampil1() # deklarasi function void
tampil2("gadis", "denpasar") # deklarasi function parameter
tampil2("agung", "canggu") # deklarasi function parameter
print(tampil3(10,20)) # deklarasi function parameter + return
hasil = tampil3(10,20) # deklarasi function parameter + return
print(hasil + 50)
ganti()
hasil_nested = nested_function(10, 20, 30)
print(hasil_nested)
hasil_rekursif = rekursif(5)
print(hasil_rekursif)

# hasil rekursif 

5 * (rekursif(4)) # step 1
5 * (4 * (rekursif(3))) # step 2
5 * (4 * (3 * (rekursif(2)))) # step 3
5 * (4 * (3 * (2 * (rekursif(1))))) # step 4
5 * (4 * (3 * (2 * (1 * (rekursif(0)))))) # step 5
5 * (4 * (3 * (2 * (1 * (1))))) # step 6

hasil_lambda = (lambda a,b : a + b)(10,20)
print(hasil_lambda)

data = {"nama": "gadis", "alamat": "denpasar"}

for key, value in data.items():
    print(f"{key} : {value}")

