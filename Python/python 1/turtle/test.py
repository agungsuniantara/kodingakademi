angka1 = int(input("masukan angka : ")) # 10
angka2 = int(input("masukan angka : ")) # 20
angka3 = int(input("masukan angka : ")) # 30

# operator logika 

operator_and = (angka1 < angka2) and (angka1 > angka3) # True and False = False
operator_or = (angka1 < angka2) or (angka1 > angka3) # True or False = True
operator_not = (angka1 < angka2) and (not(angka1 > angka3)) # True and True = True

print("hasil and : ", operator_and)
print("hasil or : ", operator_or)
print("hasil not : ", operator_not)
