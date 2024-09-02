data = open("cathrine\lecture_5\kata.txt", "r")

data2 = []

for kata in data:
    data2 = kata.split()

print(data2)

data.close()