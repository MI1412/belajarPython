from . import Database
from .Util import random_str
import time

# operasi yang ber interaksi dengan database

def create_first_data():
    penulis = input('penulis : ')
    judul = input('judul : ')
    tahun = input('tahun : ')
    
    data = Database.TEMPLATE.copy()
    data['pk'] = random_str(6)
    data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%S%z',time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE["judul"][len(judul):]
    data['tahun'] = tahun 
    
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
    