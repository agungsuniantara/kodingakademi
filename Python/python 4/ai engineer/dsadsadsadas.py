def assignment(*a):
    total = sum(a)
    data = len(a)
    return total, data
    
total, data = assignment(1, 2, 3)
result = (lambda a, b : a / b)(total, data)
print(result)  # Output: 2.0