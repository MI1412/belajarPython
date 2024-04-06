# ruang lingkup variabel global dan lokal

nama = 'imr' # <-- ini adalah variabel global

# akses variabel global dalam funct
def funct():
    print(f'fungsi menampilkan nama {nama}')
    
funct()  

# akses variabel global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama}")

# akses variabel global dalam percabangan
# if True:
#     print(f"menampilkan {nama}")
    
# ini adalah lingkup variabel lokal
def funct2(var_lokal):
    print(f'variabel lokal {var_lokal}')

funct2('ms')
# print(local_var) ini akan error krn ruang lingkup variabel local_var ada didalam funct2() 

# contoh penggunaan variabel global
# 1. penggunan 
def say_halo():
    print(f'halo {nama}')
nama = 'imron'    
say_halo()

# 2. merubah nilai variabel global
angka = 0
def ubah_angka(nilai_baru):
    
    global angka # fungsi ini digunakan untuk bisa mendapatkan akses variabel global
    angka = nilai_baru # kemudian ditulis ke variabel lokal lagi
    
print(f"sebelum dirubah = {angka}")    
ubah_angka(10)
print(f"sesudah dirubah = {angka}")

# 3. memakai loop 

angka = 0
for i in range(0,5):
    angka += i
    angka_dump = 1
    
print(angka)    
print(angka_dump) # ini tidak akan bisa diakses karena termasuk variabel lokal    

if True:
    angka = 10
    angka_dump = 10
    
print(angka)    
print(angka_dump) # ini tidak akan bisa diakses karena termasuk variabel lokal    