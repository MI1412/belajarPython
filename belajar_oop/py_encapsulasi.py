# encapsulasi digunakan buat variabel private dan mengurangi terjadinya bug
# untuk mengambil data yang dibutuhkan menggunakan getter dan setter
# getter untuk mengambil variabel dari private
# setter untuk mensetting variabel dari private

# contoh
class Yo:

    def __init__(self,name,tipe,darah):
        self.__name = name
        self.__tipe = tipe
        self.__darah = darah
        # untuk membuat objek private adalah __namevariabel
        
    # -> membuat fungsi getter/mengambil variabel private
    def getName(self):
        return self.__name
    
    def getStatus(self):
        return self.__tipe
    
    def get_darah(self):
        return self.__darah
    
    # setter atau memberi pengaturan
    def statusAttack(self,attck):
        self.__darah -= attck
        
    def change_status(self,stat):
        self.__tipe = stat    

# init
satria = Yo('satria','murid',1000)
print(satria.__dict__)

# ini tidak boleh dilakukan karena variabel private
# satria.__name = 'amir' ini tidak akan dieksekusi karena variabel private
# yang benar begini ->

# membuat nama tidak bisa dirubah oleh orang lain
print(satria.getName())

# contoh lain
print(satria.getStatus())
print(satria.get_darah())

# kenapa hasil ini none
satria.change_status('guru')
satria.statusAttack(99)

# kenapa hasil ini none
print(satria.statusAttack(8))


