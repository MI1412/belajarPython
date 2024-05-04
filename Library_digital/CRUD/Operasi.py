# operasi yang ber interaksi dengan database
from . import Database
from .Util import random_str
import time

# membuat teks baru
def create(tahun,judul,penulis):
    data = Database.TEMPLATE.copy()
    
    data['pk'] = random_str(6)
    data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%S%z',time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE["judul"][len(judul):]
    data['tahun'] = str(tahun)
    
    data_str = f'{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n'
    
    try:
        with open(Database.DB_NAME,'a',encoding='utf-8') as file:
            file.write(data_str)
    except:
        print('erorr') 
    

# jika data tidak ditemukan
def create_first_data():
    penulis = input('penulis : ')
    judul = input('judul : ')
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
    
    data = Database.TEMPLATE.copy()
    
    data['pk'] = random_str(6)
    data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%S%z',time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE["judul"][len(judul):]
    data['tahun'] = str(tahun) 
    
    data_str = f'{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n'
    
    try:
        with open(Database.DB_NAME,'w',encoding='utf-8') as file:
            file.write(data_str)
    except:
        print('erorr')        
    
def read():
    try:
        with open(Database.DB_NAME,'r') as file:
            content = file.readlines()
            return content    
    except:
        print('database eror')
        return False
    