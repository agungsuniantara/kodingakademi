def total (*a):
    jumlah_data = sum(a)
    banyak_data = len(a)
    return jumlah_data, banyak_data

hasil, banyak = total(10,20,30,40,50)

rata = (lambda a,b : a / b)(hasil, banyak)

print("rata - rata = ", rata)