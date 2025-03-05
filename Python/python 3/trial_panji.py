class pegawai:
    def __init__(self):
        self.data = {}
    
    def tambah(self,nama, status, tahun, gaji):
        self.data[nama] = [status, tahun, gaji]
    
    def edit(self, nama, status, tahun, gaji):
        for key, value in self.data.items():
            if key == nama:
                value[0] = status
                value[1] = tahun
                value[2] = gaji
            
                    
                
            
    
    def hapus(self, nama):
        # cek paramater nama apakah ada di key data / dictionary
        # jika ada data nama hapus
    
    def tampil(self):
        # panggil isi dari dictionary / data

db = pegawai()