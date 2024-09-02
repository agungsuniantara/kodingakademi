# assignment 1

nilai = int(input("masukkan nilai = "))
if(nilai > 0 and nilai <= 50):
    print("Nilai anda D")
elif(nilai > 50 and nilai <= 70):
    print("nilai anda C")
elif(nilai > 70 and nilai <= 80):
    print("nilai anda B")
elif(nilai > 80 and nilai <= 100):
    print("nilai anda A")
else:
    print("input angka yang benar")

print()

# assignment 2

nilai = int(input("masukkan nomer : "))
if (nilai % 2) == 0:
    print("nilai",nilai,"adalah bilangan genap")
else:
    print("nilai",nilai,"adalah bilangan ganjil")