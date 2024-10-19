angka = [10, 4, 28, 9]
new = []

while angka:
    max_value = max(angka)
    new.append(max_value)
    angka.remove(max_value)

print(new)