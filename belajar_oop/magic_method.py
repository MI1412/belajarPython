# magic method / Dunder Method adalah keyword yang ada dipython untuk digunakan kembali 
# magic method berguna untuk melakukan operasi method dan mengoverride bentuk method originalnya

class Manusia:
    
    # Dunder Method 1.
    def __init__(self,nama,stat):
        self.nama = nama
        self.stat = stat
    
    # dunder method 2.
    # repr digunakan untuk debugging
    def __repr__(self):
        return f'\nini adalah REPR {self.nama} \nstatus : {self.stat}'
    
    # dunder method 3. 
    # str digunakan kalau programnya sudah jadi
    def __str__(self):
        return f'\nini adalah STR {self.nama} \nstatus : {self.stat}'
    
    def __add__(self,objek):
        return self.nama + objek.nama
        
    def __dict__(self):
        return f'\nDICTIONARY\nnama : {self.nama} \nstat : {self.stat}'
musa = Manusia('Musa','pelajar')
amir = Manusia('Amir','mahasiswa')

# sebelum menggunakan repr
# <__main__.Manusia object at 0x000002643179A270>

# setelah menggunakan repr 'ini adalah objek'
print(musa.__repr__())
print(amir.__str__())
print(amir + musa)
print(musa.__dict__())
print(amir.__dict__())












