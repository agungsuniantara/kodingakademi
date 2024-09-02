search_text = "gunung"
search_text2 = "Gunung"
ganti = "pegunungan"
gunung = []

with open('file\search_data.txt', 'r') as file:
    data = file.read()
    test = data.split()
    for i in test:
        if i == search_text or i == search_text2:
            gunung.append(i)

with open('file\search_data.txt', 'r') as file:
    data = file.read()
    data = data.replace(search_text, ganti)
    data = data.replace(search_text2, ganti)

with open('file\search_data.txt', 'w') as file:
    file.write(data)
    
print(f"jumlah gunung = {len(gunung)}")