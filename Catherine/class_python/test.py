def penjumlahan(n):
    if n == 1:  # Base case
        return 10
    else:  # Recursive case
        return n + penjumlahan(n - 1)

def faktorial(n):
    if n == 0:  # Base case
        return 2
    else:
        return n * faktorial(n - 1)

hasil1 = penjumlahan(3)
hasil2 = faktorial(4)
print(hasil1)
print(hasil2)
