nama = input("masukan nama : ")
alamat = input("masukan alamat : ")
umur = input("masukan umur : ")

data = [nama, alamat, umur]

data = [nama + "\n", alamat + "\n", umur + "\n"]

with open("file/test.txt", "w") as f:
    f.writelines(data)