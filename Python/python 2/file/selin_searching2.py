with open("search_data.txt", "r") as f:
    data = f.read()
    data_lower = data.lower()
    jumlah_gunung = data_lower.count("gunung")

data_lower = data_lower.replace("gunung", "pegunungan")

with open("search_data.txt", "w") as f:
    f.write(data_lower)

print(f"Jumlah kata 'gunung' yang ditemukan: {jumlah_gunung}")