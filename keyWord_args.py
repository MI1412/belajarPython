# keywords args
import os
def fungsi(nama,tinggi,berat):
    # funct biasa
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')
    
fungsi('imron',12,19)    

print('\n')


# memakai keywords args dengan memakai bintang 2 atau **
def fungsi(**kwargs):
    nama = kwargs['nama'] # membuat variabel
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']
    
    print(kwargs['nama']) # mengakses keywords dengan keynya nama
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}') 
fungsi(nama = 'imron',tinggi =12,berat = 19) # hasil yang dikeluarkan akan berupa dictionary

#  studi kasus

def math(*args, **kwargs):
    if kwargs['option'] == 'tambah':
        output = 0
        for angka in args:
            output = angka1 + angka2
        print('\nini operasi penjumlahan')        
    elif kwargs['option'] == 'kali':
        for angka in args:
            output = angka1 * angka2
        print('\nini operasi perkalian')   
    elif kwargs['option'] == 'kurang':
        for angka in args:
            output = angka1 - angka2
        print('\nini operasi pengurangan')  
    elif kwargs['option'] == 'bagi':
        for angka in args:
            output = angka1 / angka2
        print('\nini operasi pembagian') 
    else:
        print('operasi matematika yang anda masukkan salah !')   
    return output   
print('\n')
while True:
    os.system('clear')
    angka1 = int(input('masukkan angka ke-1 : '))
    angka2 = int(input('masukkan angka ke-2 : '))
    opsi = input('masukkan opsi operasi matematika : ')
    hasil = math(angka1,angka2, option = opsi)
    print(f'hasil {opsi} = {hasil}')
    decision = input('\napakah ingin mengulangi operasi diatas (y/n)? ')
    if decision == 'n':
        break
print('end program')    