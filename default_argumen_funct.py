# default argumen funct
# def funct(argumen):

# contoh funct memakai default argumen funct(argumen = nilai default):

# contoh 1
def halo(name = 'kamu'):
    # funct dengan default argumen
    print(f"halo {name}")
    
halo('dev')    
halo()



# contoh 2
def hello(nama,pesan = 'sukses'):
    # fungsi dengan satu input biasa dan satu input default argumen
    print(f"hai {nama} {pesan}")

hello('imron','selamat')   
hello('imron') 

# contoh 3

def pangkat(angka,pangkat):
    hasil = angka**pangkat
    return hasil

print(pangkat(2,2))

# mengakses argumen funct langsung 
hasil = pangkat(angka=8,pangkat=2)
print(hasil)
