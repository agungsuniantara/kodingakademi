def test(*a):   # * = args
    result = sum(a)
    return result

hasil = test(1,2,3,4,5,6,7,8,9,10)

rata = (lambda a,b : a / b)(hasil,10)

print(f"rata-rata: {rata}")
