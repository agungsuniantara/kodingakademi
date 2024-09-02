data = {}
filename = "lecture_5\kata.txt"

def total_population(data, filename):
    with open(filename, 'w') as file_open:
        for key, value in data.items():
            file_open.write(f"{key}: {value}\n")

    with open(filename, 'r') as file_read:
        print(file_read.read())

while True:
    city = input("Masukkan nama kota: ")
    population = input("Masukkan populasi: ")
    data[city] = population
    ask = input("Ingin menambah data? (ya/tidak): ")
    if ask.lower() == "tidak":
        break

total_population(data, filename)
