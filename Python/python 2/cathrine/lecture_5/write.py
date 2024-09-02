data = open("cathrine\lecture_5\kata.txt", "w")
tulis = data.write("ini teks baru")

data = open("cathrine\lecture_5\kata.txt", "r")
baca = data.read()
print(baca)