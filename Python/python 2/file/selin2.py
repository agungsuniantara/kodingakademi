nama = input("Masukkan nama Anda: ")
age = input("Masukkan umur Anda: ")
address = input("Masukkan alamat Anda: ")

with open("data.txt", "w") as f:
    f.write(f"Nama | Umur | Alamat\n")

with open("data.txt", "a") as f:
    f.write(f"{nama} | {age} | {address}\n")