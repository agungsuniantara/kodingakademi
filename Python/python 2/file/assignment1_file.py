nama = input("masukan nama : ")
alamat = input("masukan alamat : ")
umur = input("masukan umur : ")

data = [nama, alamat, umur]

f = open("file/test.txt", "w")
f.writelines(data)
f.close()