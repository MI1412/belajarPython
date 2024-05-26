class Siswa:
    # private class variabel
    __jumlah = 0
    def __init__(self,name):
        self.__name = name
        Siswa.__jumlah += 1

    # jika mencoba buat getter maka sama saja eror
    # method ini hanya berlaku untuk objek 
    def getJumlah(self):
        return Siswa.__jumlah 
    
    # method ini tidak berlaku untuk objek tapi berlaku untuk class
    def getJumlah():
        return Siswa.__jumlah    
    
    # static method yang bernama decorator untuk menempelkan method ke class dan objek
    @staticmethod # <-
    def getJumlah1():
        return Siswa.__jumlah    
    
    # selain static method ada yang namanya class method untuk menempelkan funct ke class dan objek 
    # perbedaan classmethod dengan s
    @classmethod
    def getJumlah2(cls):
        return cls.__jumlah
    
ucup = Siswa('ucup')

# print(Siswa.__jumlah) ini akan eror karena mengandung private variabel

# eror karena ada argumen self
satria = Siswa('satria')
print(f"urutan satria berada : {satria.getJumlah1()}") # ->

# ini akan eror karena didalam funct getJumlah ada variabel private
# print(satria.getJumlah())
edo = Siswa('edo')
amir = Siswa('amir')
print(f"jumlah siswa : {Siswa.getJumlah1()}") # ->

# untuk menempelkan variabel private ke class menggunakan @classmethod
print(f"ini menggunakan class method : {Siswa.getJumlah2()}")