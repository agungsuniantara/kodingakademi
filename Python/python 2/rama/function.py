def total(*a):
    total = sum(a)
    panjang = len(a)
    return total, panjang 

hasil,panjang = total(10,20,30,40,50)

rata = (lambda a,b : a / b)(hasil, panjang)
print(rata)