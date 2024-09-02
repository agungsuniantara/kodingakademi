data = open("cathrine\lecture_5\kata.txt", "a")
teks = data.write("\nnama : catherine \numur = 18 \nalamat = denpasar")

data = open("cathrine\lecture_5\kata.txt", "r")
baca = data.read()
print(baca)