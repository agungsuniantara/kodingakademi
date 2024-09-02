search_text = "Koding Akademi"
replace_text = "Koding Akademi 2.0"
with open('file\kodingakademi.txt', mode='r') as file:
	data = file.read()
	data = data.replace(search_text, replace_text)
with open('file\kodingakademi.txt', mode='w') as file:
	file.write(data)