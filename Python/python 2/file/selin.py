# file operation (r = read, w = write, a = append, r+ = read and write)

# reading file (r)

with open("nama.txt", "r") as f:
    print(f.read()) # read = membaca seluruh isi file

with open("nama.txt", "r") as f:
    kata = f.readlines()
    print(kata[0]) # membaca baris pertama file
    print(kata[1]) # membaca baris kedua file
    print(kata[2]) # membaca baris ketiga file
    
    for i in kata:
        print(i.strip()) # strip = menghapus karakter newline (\n) pada setiap baris

# writing file (w)

teks = "hello world"
with open("kalimat.txt", "w") as f:
    f.write(teks) # write = menulis teks ke dalam file, jika file tidak ada maka akan dibuat, jika file sudah ada maka akan ditimpa

# append file (a)

add_word = "hello python"
with open("kalimat.txt", "a") as f:
    f.write("\n" + add_word) # append = menambahkan teks ke dalam file, jika file tidak ada maka akan dibuat, jika file sudah ada maka akan ditambahkan di akhir file
    
# read and write file (r+)

with open("kalimat.txt", "r+") as f:
    print(f.read())
    f.write("\nhello world python")
    
with open("kalimat.txt", "r") as f:
    print(f.read()) # read = membaca seluruh isi file

# csv file operation

import csv 

# csv list

data = []

with open("dataset.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        data.append(row)

labels = data.pop(0) # menghapus header pada dataset
print(labels) # menampilkan header pada dataset
print(data) # menampilkan data pada dataset

# csv dictionary 

data_dict = []

with open("dataset.csv", "r") as f:
    reader = csv.DictReader(f, delimiter=",")
    for row in reader:
        data_dict.append(row)

print(data_dict) # menampilkan data pada dataset sebagai dictionary

for i in data_dict:
    if i["Nama"] == "agung":
        print(i) # menampilkan data pada dataset yang memiliki nama "Agung"
        
# writing csv file

with open("dataset.csv", "a") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["3", "wahyu", "PHP", "badung"]) # menambahkan data baru ke dalam dataset

with open("dataset.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        print(row) # menampilkan seluruh data pada dataset setelah penambahan data baru

# writing csv file with dictionary

kolom = ["ID", "Nama", "Bahasa Pemrograman", "Kota"]

with open("data_baru.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=kolom, delimiter=",")
    writer.writeheader() # menulis header pada dataset
    writer.writerow({"ID": "1", "Nama": "agung", "Bahasa Pemrograman": "python", "Kota": "denpasar"}) # menambahkan data baru ke dalam dataset
    writer.writerow({"ID": "2", "Nama": "wahyu", "Bahasa Pemrograman": "PHP", "Kota": "badung"}) # menambahkan data baru