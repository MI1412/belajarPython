# property getter dan setter
class Siswa:
    
    
    def __init__(self,nama,stat,darah):
        self.nama = nama
        self.__stat = stat
        self.__darah = darah
        # tetapi kalau self.info ditaruh dalam variabel ini maka variabel name tidak terupdate
        # self.info = '\nnama : {} \nstatus : {}'.format(self.nama,self.__stat)
    # @property akan membuat function dalam class dirubah menjadi variabel dalam objek
    
    # @staticmethod
    # def getName():
    #     return Siswa.__nam
        
    # keunggulan dari @property bisa merubah objek secara dinamis atau terupdate contoh ->    
    @property
    def info(self):
        return '\nnama : {} \nstatus : {}'.format(self.nama,self.__stat)
    
    # ini akan none karena belum diambil dari objek
    @property
    def darah(self):
        pass
    
    # ini getter untuk variabel private
    @darah.getter
    def darah(self):
        return self.__darah
    
    # ini setter untuk bisa merubah variabel menjadi publik
    @darah.setter
    def darah(self,input):
        self.__darah = input

    @darah.deleter
    def darah(self):
        self.__darah = None

imron = Siswa('imron','murid',9000)

# variabel ini akan mudah diakses oleh client jadi kita harus sembunyikan variabel info
# print(imron.info)

print(f"\nsebelum dirubah : {imron.info}\n")
print(f"isi dari objek {imron.nama} : {imron.__dict__}") # disini tidak ada variabel info tapi info dapat diambil sebagai method

# ->
imron.nama = 'yayaya'
print(f"\nsesudah sesudah dirubah : {imron.info}\n")

print(f'\nini darah sebelum dirubah : {imron.darah}')
print(f"isi dari objek {imron.nama} : {imron.__dict__}\n") 


imron.darah = 1000
print(f'ini darah setelah dirubah : {imron.darah}')
print(f"isi dari objek {imron.nama} : {imron.__dict__}") 

del imron.darah
print(f'\nhapus darah : {imron.darah}')
print(f"isi dari objek {imron.nama} : {imron.__dict__}") 