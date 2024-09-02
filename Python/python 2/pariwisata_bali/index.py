import os
import msvcrt

data_directory = r"pariwisata_bali\datanew"
list_file = r"pariwisata_bali\datanew\all.txt"


def list_destination():
    with open(list_file, "r") as file:
        data = file.readlines()
        for i in data:
            print(i.strip())  # Remove newline characters


def load_destinations_from_file(file_path):
    destinations = []
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for line in file:
                destinations.append(line.strip())
    return destinations


def kategori():
    destination_type = input(
        "\nPilih Kategori wisata yang ingin kamu kunjungi :\n - Pantai\n - Alam (selain pantai)\n - Seni\n - Budaya \nPilihanmu (masukkan teks): "
    )
    file_path = os.path.join(data_directory, f"{destination_type.lower()}.txt")
    destinations = load_destinations_from_file(file_path)
    if destinations:
        print("\nPilih salah satu destinasi berikut:")
        for index, destination in enumerate(destinations, start=1):
            print(f"{index}. {destination}")
            
        user_choice = input("Pilihanmu (masukkan teks): ")
        file_path2 = os.path.join(data_directory, f"{user_choice.lower()}.txt")
        lanjutan = load_destinations_from_file(file_path2)
        if lanjutan:
            print("\nBerikut adalah tempat wisata sesuai kategori yang kamu pilih : ")
            for index, destination in enumerate(lanjutan, start=1):
                print(f"{index}. {destination}")
        return ""

while True:
    pilihan = input(
        "Selamat Datang! Ayo tentukan destinasi wisata di Pulau Bali sesuai keinginanmu.\n1. Daftar Seluruh Wisata\n2. Pilih wisata berdasarkan kategori\n0. Keluar\nPilihanmu (masukkan angka): "
    )
    if pilihan == "1":
        list_destination()
    elif pilihan == "2":
        kategori()
    elif pilihan == "0":
        break
    print("\nPress any key to continue...")
    msvcrt.getch()  # Menunggu pengguna menekan tombol
    os.system("cls")  # Menghapus layar
