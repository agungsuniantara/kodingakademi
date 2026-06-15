search_text = "gunung"
ganti = "pegunungan"
gunung = [] 

with open('file\search_data.txt', 'r') as file:
    data = file.read()
    test = data.split(" ") 
    for i in test:
        if i == search_text.lower():
            gunung.append(i)

with open('file\search_data.txt', 'r') as file:
    data = file.read()
    data = data.replace(search_text, ganti)

with open('file\search_data.txt', 'w') as file:
    file.write(data)
    
print(f"jumlah gunung = {len(gunung)}")