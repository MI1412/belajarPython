# view itu menampilkan hasil input
from . import Operasi
from . import Database


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
            data = Database.TEMPLATE.copy
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
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        
        print(f'{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}',end='')
    
    
    
    # footer
    print(100*'='+'\n')