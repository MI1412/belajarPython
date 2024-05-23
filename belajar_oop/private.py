# private

class HEHE:
    # class variabel 
    jumlah = 0
    __privateJumlah = 0

    # ini semua adalah variabel publik
    def __init__(self,nama,stat):
        self.nama = nama
        self.stat = stat

        # variabel instance private tidak bisa diakses
        self.__private = 'private'

        # variabel instance protective
        # kenapa diberi _ di protected karena agar menandakan sebuah variabel ini didalam class saja tidak boleh dirubah 
        self._protected = 'protected'



yayayya = HEHE('lol','student') 

print('\ncontoh dari Private variabel')
print(yayayya.__dict__)
# jika kita coba akses yayayaya dengan private akan eror
# print(yayayya.__private)
# jika mengakses secara langsung maka akan dibuat objek baru
yayayya.private = 'tes' # ini adalah penugasan variabel diluar class seperti menambahkan variabel
print(f"\n{yayayya.__dict__}\n")    

print('contoh dari Protected variabel')
print(f"{yayayya.__dict__}")

yayayya._protected = 'tes'
print(f"\n{yayayya.__dict__}")
print(yayayya._protected)
print(f"\n{HEHE.__dict__}")
