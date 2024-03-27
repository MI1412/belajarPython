import datetime
import os
import random
import string

# template dict siswa
siswa_template = {
    'nama':'nama',
    'nik':'910998',
    'ttl': datetime.datetime(2006,12,12)
}

data_siswa = {}

while True:
    os.system('clear') # membuat auto clear ketika menjalankan program
    print(f"\n{'selamat datang':^50}")
    print(f"{'data siswa':^50}")
    print('='*49)
    # from keys
    siswa = dict.fromkeys(siswa_template.keys()) # membuat variabel dict kosong
    siswa['nama'] = input("nama siswa \t\t\t: ") # (nama key) memasukkan variabel string ke dictionary
    siswa['nik'] = int(input("no nik siswa \t\t\t: "))
    tahun_lahir = int(input("tahun lahir siswa (yyyy)\t: "))
    bulan_lahir = int(input("bulan lahir siswa (1-12)\t: "))
    tanggal_lahir = int(input("tanggal lahir siswa (1-31)\t: "))
    siswa['ttl'] = datetime.datetime(tahun_lahir,bulan_lahir,tanggal_lahir)

    key = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))# membuat random key 
    data_siswa.update({key:siswa})
    
    print("-"*49)
    print(f"{'output':>25}")
    print("-"*49)
    print(f"{'key':<9} {'nama':<10} {'nik':<13} {'ttl':<15}")
    print("-"*49)

# loop dict
    for siswa in data_siswa:
        key = siswa
        nama = data_siswa[key]['nama']
        nik = data_siswa[key]['nik']
        lahir = data_siswa[key]['ttl'].strftime("%x")
        
        print(f"\n{key:<9} {nama:<10} {nik:<13} {lahir}")
        
    print('\n')
    is_Done = input('sudah selesai (y/n)? ')
    if is_Done == 'y':
        break
    
print('\nakhir program')    