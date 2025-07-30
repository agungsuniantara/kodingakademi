class test:
    def __init__(self):
        self.data = {}
    
    def simpan(self, a, b, c, d):
        nim = d[2:] + a 
        self.data[nim] = [b,c,d]
    
    def tampil(self):
        print("Data mahasiswa : ")
        for key, value in self.data.items(): # key = 21099, value = ["dsada", "dasdas"]
            print(f"Nim : {key}")
            print(f"Nama : {value[0]}")
            print(f"Alamat : {value[1]}")
            print(f"Tahun : {value[2]}")
        

data1 = test()

nim = input("masukan nim : ")
nama = input("masukan nama : ")
alamat = input("masukan alamat : ")
tahun = input("masukan tahun : ")

data1.simpan(nim, nama, alamat, tahun)
data1.tampil()