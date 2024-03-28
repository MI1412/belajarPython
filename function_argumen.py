# function argumen / mengisi nilai pada function
# contoh

# membuat funct sapaan
def hello(nama): # nama adalah parameter atau value / nilai
    # badan dalam fungsi
    print(f'halo {nama}') # menampilkan parameter / value / nilai

hello('imron') # nilai / parameter dari nama diisi imron bertipe string

# membuat funct tambah
def funct_tambah(angka1,angka2):
    hasil = angka1 + angka2
    print(f"hasil pertambahan = {hasil}")
    
funct_tambah(9,8)    

# funct list
def halo(murid):
    data_murid = murid.copy()
    for murid in data_murid:
        print(f'halooooo {murid}')

kelas = ['ucup','asep','madun','amir']
halo(kelas)