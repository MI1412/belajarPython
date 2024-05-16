# method adalah perilaku pada sebuah objek / interaksi antar objek
class nama_siswa:
    jumlah = 0
    def __init__(self,name,umur):
        self.name = name
        self.umur = umur
        
# contoh method tanpa return atau dipanggil void function
    def say(self): # memakai self digunakan untuk menempel ke objek
        print('halo ...', self.name)
        nama_siswa.jumlah +=1
        
# contoh method dengan argumen 
    def tambah_umur(self,up):
        self.umur += up
# contoh method dengan return 
    def ambil_umur(self):
        return self.umur
nama_siswa1 = nama_siswa('hehehha',90)
nama_siswa2 = nama_siswa('lol',99)

print(nama_siswa1.__dict__)        
print(nama_siswa2.__dict__)        

# void function
nama_siswa1.say()
nama_siswa2.say()

# method dengan argumen 
nama_siswa1.tambah_umur(9)
print(nama_siswa1.umur)

# method dengan return
print(nama_siswa2.ambil_umur())