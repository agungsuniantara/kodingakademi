import csv

data_dict = []

with open("datsetFinal.csv", "r") as f:
    reader = csv.DictReader(f, delimiter=",")
    for row in reader:
        data_dict.append(row)

men = []
woman = []

for i in data_dict:
    if i["Kelamin"] == "Laki-laki":
        men.append(i)
    else:
        woman.append(i)

print("Data Laki-laki:", len(men))
print("Data Perempuan:", len(woman))

kolom = data_dict[0].keys()

with open("data_laki.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=kolom, delimiter=",")
    writer.writeheader()
    writer.writerows(men)

with open("data_perempuan.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=kolom, delimiter=",")
    writer.writeheader()
    writer.writerows(woman)