# view itu menampilkan hasil input
from . import Operasi
from . import Database

def delete_console():
    read_console()
    while(True): 
        print('silahkan pilih data yang ingin dihapus ')
        no_buku = int(input('No buku : '))
        # mengambil index no_buku
        data_buku = Operasi.read(index = no_buku)
        
        if data_buku:
            # memformat data_buku
            data_break = data_buku.split(',')        
            pk = data_break[0]
            date_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]
        
            # data yang dihapus 
            print('\n'+'='*100+f'\n Data no buku {no_buku} ini akan dihapus ')
            print(f'1. Penulis\t: {penulis:.40}')
            print(f'2. Judul\t: {judul:.40}')
            print(f'3. Tahun\t: {tahun:4}')
            print(100*'-')
            
            is_done = input(f'Yakin data buku {no_buku} ingin dihapus (Y/N) ? ') 
            
            if is_done == 'y' or is_done == 'Y':
                Operasi.delete(no_buku)
                break            
        else:
            print('buku tidak ditemukan coba lagi ')
            
            
    print('\nData berhasil dihapus !')        



# mengupdate data
def update_console():
    read_console()
    while(True): 
        no_buku = int(input('pilih no buku yang ingin diupdate : '))
        
        # mengambil index no_buku
        data_buku = Operasi.read(index = no_buku)
        
        if data_buku:
            break
        else:
            print('buku tidak ditemukan coba lagi ')
    # memformat data_buku
    data_break = data_buku.split(',')        
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]
    
    # input data yang dirubah
    while(True):
        print('\n'+'='*100+'\nsilahkan ubah data yang anda inginkan')
        print(f'1. Penulis\t: {penulis:.40}')
        print(f'2. Judul\t: {judul:.40}')
        print(f'3. Tahun\t: {tahun:4}')
        print(100*'-')
        
        user_option = int(input('pilih data yang ingin diubah (1,2,3) : '))
        
        match user_option:
            case 1:
                penulis = input('Penulis\t: ')
            case 2:
                judul = input('Judul\t: ')
            case 3:
                while(True):
                    try:
                        tahun = int(input('Tahun\t: '))
                        panjang_tahun = len(str(tahun))
                        if panjang_tahun == 4 and panjang_tahun == 4 :
                            break
                        
                        else:
                            print(f'tahun yang anda masukkan {panjang_tahun} digit angka , seharusnya ada 4 digit angka (yyyy)')
                            
                    except:
                        print('tahun harus angka, masukkan angka lagi')    
            case _:
                print('tidak ada opsi yang dipilih masukkan lagi') 
                
        # view data baru
        print('\n'+'='*100+'\nData Berhasil Diupdate')
        print(f'1. Penulis\t: {penulis:.40}')
        print(f'2. Judul\t: {judul:.40}')
        print(f'3. Tahun\t: {tahun:4}')
        print(100*'-')
        
        is_done = input('Apakah sudah selesai update data (Y/N) ? ')        
        
        
        if is_done == 'y':
            break
    Operasi.update(no_buku,pk,data_add,tahun,judul,penulis)    



# membuat file
def create_console():
    print('\n\n'+'='*100)
    print('silahkan tambahkan data \n')
    penulis = input('Penulis\t: ')
    judul = input('Judul\t: ')
    while(True):
        try:
            tahun = int(input('Tahun\t: '))
            panjang_tahun = len(str(tahun))
            data = Database.TEMPLATE.copy()
            if panjang_tahun == 4 and panjang_tahun == 4 :
                break
            
            else:
                print(f'tahun yang anda masukkan {panjang_tahun} digit angka , seharusnya ada 4 digit angka (yyyy)')
                
        except:
            print('tahun harus angka, masukkan angka lagi')
    Operasi.create(tahun,judul,penulis)
    print('\ndata berhasil ditambahkan')
    read_console()

# membaca file 
def read_console():
    data_file = Operasi.read()
    index = 'No'
    judul = 'Judul'
    penulis = 'Penulis'
    tahun = 'Tahun'
    # header
    print('\n'+'='*100)
    # judul
    print(f'{index:4} | {judul:40} | {penulis:40} | {tahun:4}')
    print('-'*100)
    
    # data
    for index,data in enumerate(data_file):
        data_break = data.split(',')
        pk = data_break[0]
        data_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        
        print(f'{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}',end='')
    
    
    
    # footer
    print(100*'='+'\n')