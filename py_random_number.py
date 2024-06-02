import random

# melihat method dalam random number
# isi = dir(random)
# print(f'isi dari module {random} : {isi}')

# menampilkan cara menggunakan module tersebut 
# help(random)
while(True):
    random_number = random.randrange(0,100)
    input_user = int(input('masukkan angka : '))
    print(f'angka yang dipilih user {input_user} dengan angka random {random_number}')
    validasi = input_user == random_number
    if validasi:
        print('selamat')
        break
    else:
        print('angka tidak cocok')
