matrix1 = [
    [1,2],
    [3,4]
]

a = matrix1[0][0] * matrix1[1][1] -  matrix1[0][1] * matrix1[1][0]
option = 1 / a 
invers = [
    [(option * matrix1[1][1]), -(option * matrix1[0][1])],
    []
]