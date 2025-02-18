a = [
    [10,20],
    [30,40]
]

det = (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])

hitung = 1 / det

invers = [
    [hitung * a[1][1], -(hitung * a[0][1])],
    [-(hitung * a[1][0]), hitung * a[0][0]]
]

print(invers)