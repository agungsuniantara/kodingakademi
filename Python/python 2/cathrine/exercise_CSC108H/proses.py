text = open("python 2/cathrine/exercise_CSC108H/data.txt", "r")

data_split = []

for i in text:
    data_split = text.split()

print(data_split)

text.close()