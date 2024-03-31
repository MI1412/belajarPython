# latihan funct membuat program menghitung luas dan keliling persegi panjang
import os

def header():
    # funct header
    # header
    os.system('clear')
print(f'{"program menghitung luas":^40}')
print(f'{"dan keliling persegi panjang":^40}')
print("-"*40)

def input_user():
    # wadah input user
    lebar = int(input('\nmasukkan nilai lebar : '))
    panjang = int(input('masukkan nilai panjang : '))
    return lebar,panjang
    
def hitung_luas(lebar,panjang):
    # hitung luas
    return lebar*panjang

def  hitung_keliling(lebar,panjang):
    # hitung keliling
    return 2*(lebar + panjang)





























while True:
    header()
    lebar,panjang = input_user()
    print(f"luas = {hitung_luas(lebar,panjang)}")
    print(f"keliling = {hitung_keliling(lebar,panjang)}")
    keliling = hitung_keliling(lebar,panjang)
    isContinue = input('apakah lanjut (y/n) : ')
    if isContinue == "n":
        break

# note untuk pembuatan funct harus ada 1 fungsi
print('program selesai')