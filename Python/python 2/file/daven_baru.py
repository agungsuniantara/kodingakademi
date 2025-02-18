import csv

data_cowok = []
data_cewek = []

with open('Python/python 2/file/datsetFinal.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    no = 1
    for row in csv_reader:
        if row["Kelamin"] == "Laki-laki":
            data_cowok.append(row)
        else:
            data_cewek.append(row)

