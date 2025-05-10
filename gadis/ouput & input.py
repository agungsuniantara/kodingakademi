nama = "gadis"
alamat = "badung"
umur = "19 tahun"

print("nama :", nama, "alamat :", alamat, "umur :",umur)
print(f"nama : {nama} alamat : {alamat} umur : {umur}")
print("nama : {} alamat : {} umur : {}".format(alamat, nama, umur))

nama = input("masukan nama : ")
umur = int(input("masukan umur : "))
umur2 = float(input("masukan umur : "))

print(f"nama = {nama} tipe data = {type(nama)}")
print(f"umur = {umur} tipe data = {type(umur)}")
print(f"umur2 = {umur2} tipe data = {type(umur2)}")