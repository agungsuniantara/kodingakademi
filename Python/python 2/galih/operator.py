angka1 = 20
angka2 = 30
angka3 = 40

operator_and = angka1 > angka2 and angka2 < angka3 # (false and true)
operator_or = angka1 > angka2 or angka2 < angka3 # (false or true)
operator_not = not(angka1 > angka2) and angka2 < angka3 # (true and true)

print(operator_and)
print(operator_or)
print(operator_not)