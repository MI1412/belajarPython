# exception, try, except
# exception akan terjadi saat program mengalami eror pada saat runtime

# contoh :
# data_input = int(input('masukkan angka : '))
# # ketika user input 0 maka terjadi runtime eror

# hasil = 10/data_input

# print(hasil)

# contoh sederhana untuk menangkap exception
from math import nan

# data_input = int(input('masukkan angka : '))
# hasil = nan


# try: # try akan mencoba input dari user
#     hasil = 10/data_input
# except: # jika terjadi kesalahan / eror pada saat runtime
#     print("input tidak boleh 0")

# print(f"hasil input = {hasil}")


# contoh diaplikasi :

# # 1. 
# while(True):
#     angka = int(input('masukkan angka bagi : '))
#     try:
#         hasil = 10/angka
#         print(f"\nhasil = {hasil}")
#         is_done = input('lanjutkan (y/n)?')
#         if is_done == 'n':
#             break
#     except:
#         print("pembagi 0 silahkan masukkan lagi !!")
            
# print("\nend program 1")    

# # 2. 
# try: # mencoba syntax di bawah ini
#     with open('data_4.txt','r') as file:
#         print(file.read()) # aslinya ini itu eror karena tidak ada filenya

# except: # except dalam bhs inggris artinya kecuali dari percobaan diatas  akan dibuat pesan eror dan menjalankan solusi dari eror
#     print("filenya ga ada, mau buat baru ")
#     with open('data_4.txt','w',encoding='utf-8') as file:
#         file.write('ini file baru')

# print('\nend program 2')            

# contoh membuat exception
from numbers import Number
def tambah(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number):   # membuat validasi
        raise "input harus angka"
    return a+b
print(tambah(9,8))

# menangkap exception berdasarkan tipenya

# contoh 1.
angka = 0
# try:
#     hasil = 10/angka
# except Exception as error_message:
#     print(error_message)    

# contoh 2.
try:
    hasil = 0/angka
except ZeroDivisionError as error_message:
    print(error_message)