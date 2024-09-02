data = open("file\mode.txt", "r+")
teks = data.read()
print(teks)

teks = "\nBelajar di Koding Akademi"
data.write(teks)
data.close()
