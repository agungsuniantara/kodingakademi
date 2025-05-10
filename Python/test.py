# function kwargs (use single variable to contain many key and value)
def show2(**a): # ** = kwargs
    print(a)

show2(name="panji", address = "denpasar")

# function args (use single variable to contain many value)
def add(*a): # * = args
    result = sum(a)
    return result

assignment = add(1,2,3,4,5, 6, 7, 8, 9, 10)
print(f"result using args = {assignment}")

mean = (lambda a,b : a / b)(assignment, 10)
print(f"mean = {mean}")




