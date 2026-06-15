search = "Koding Akademi 2.0"
replace = "Koding Akademi"

with open("kodingakademi.txt", "r") as f:
    data = f.read()
    
data = data.replace(search, replace)

with open("kodingakademi.txt", "w") as f:
    f.write(data)
