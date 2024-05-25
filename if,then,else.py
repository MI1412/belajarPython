# if untuk menjalankannya
# then untuk melanjutkan dipython then adalah elif
# else adalah hasil false
import os
str = input('masukkan test string : ')
if len(str)< 6:
    print('string sangat pendek')
    print('tolong masukkan minim 6 karakter')

number = int(input('masukkan angka : '))

if number % 2 == 0:
    print(f'{number} adalah genap')
else:
    print(f'{number} adalah ganjil')        

# contoh berikut menyatakan bentuk segitiga

while(True):
    os.system('clear')
    a = int(input('lebar sisi a : '))
    b = int(input('lebar sisi b : '))
    c = int(input('lebar sisi c : '))
    if a != b and b != c and a != c :
        print('segita tidak sama sisi')
    elif a == b and b == c:
        print('segitiga sama sisi')    
    else:
        print('segitiga sama kaki')    
    isdone = input('selesai (y/n)? ')  
    if isdone == 'y':
        break
    else:
        os.system('clear')

