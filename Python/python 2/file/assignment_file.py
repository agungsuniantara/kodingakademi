import csv

data_cowok = []
data_cewek = []

with open('datsetFinal.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if row['Kelamin'] == 'Laki-laki':
            data_cowok.append(row)
        else:
            data_cewek.append(row)
            
# Menyimpan data cowok ke file CSV
with open('data_cowok.csv', 'w', newline='') as cowok_file:
    cowok_writer = csv.DictWriter(cowok_file, fieldnames=csv_reader.fieldnames)
    cowok_writer.writeheader()
    cowok_writer.writerows(data_cowok)

# Menyimpan data cewek ke file CSV
with open('data_cewek.csv', 'w', newline='') as cewek_file:
    cewek_writer = csv.DictWriter(cewek_file, fieldnames=csv_reader.fieldnames)
    cewek_writer.writeheader()
    cewek_writer.writerows(data_cewek)
    

a = 5
count = 0 # 1 # 6

while count <= a:
    print("*****")
    count += 1

