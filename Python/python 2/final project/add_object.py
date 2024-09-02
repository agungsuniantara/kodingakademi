class staff:
    def __init__(self, nama, umur) :
        self.nama = nama
        self.umur = umur

class data:
    def __init__(self):
        self.dict = {}
    
    def tambah_data(self, staff):
        nama = staff.nama
        self.dict[nama] = staff

manager = staff("agung", 25)
array = data()

print(f"Nama : {manager.nama}")
print(f"Umur : {manager.umur}")

array.tambah_data(manager)
print(array.dict)
print(array.dict["agung"])
    