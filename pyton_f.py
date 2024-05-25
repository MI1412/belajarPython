import os
while(True):
    os.system('clear')
    print(f"ini sebelum : {dir()}")

    # funct tanpa return
    def p():
        pass

    # akan menampilkan alamat memori fungsi
    # dan memberi ruang untuk funct
    print(f"\nini adalah alamat funct : {p}")
    print(f"ini sesudah ditambah funct : {dir()}")

    # funct tanpa argumen 
    def say():
        return 'halo'
    print(say())
    print(f"\nini adalah alamat funct : {say}")
    print(f"ini sesudah ditambah funct : {dir()}")
    isdone = input('apakah sudah selesai y/n ? ')
    if isdone == 'y':
        break
import math
while(True):
    os.system('clear')
    # contoh dalam matematika
    print(f"\nisi direktori math : {dir(math)}")
    math.pi
    input_volume = int(input('masukkan nilai volume : '))
    # funct memakai argumen 
    def volume(r):
        """ ini adlah docstring mengembalikan nilai r"""
        v = (4.0/3.0) * math.pi * r**3
        return v
    print(f'\nini volume ke{input_volume} : hasil {volume(input_volume)}')
    isdone = input('apakah sudah selesai y/n ? ')
    if isdone == 'y':
        break

# menghitung luas segitiga
while(True):
    os.system('clear')
    base = int(input('masukkan nilai base : '))
    height = int(input('masukkan nilai tinggi : '))
    def triangle_area(b,h):
        """ mengembalikan nilai b = base h = height """
        return 0.5 * b * h
    print(f'ini adalah menghitung area segitiga : {triangle_area(base,height)}')
    isdone = input('apakah sudah selesai y/n ?  ')
    if isdone == 'y':
        break




while(True):
    os.system('clear')
    print('konversi lebar kaki dan inci ke cm')
    feet = int(input('masukkan angka : ')) 
    inch = int(input('masukkan angka : ')) 
    
    # contoh funct keyword argumen
    def cm(feet = 0, inch = 0): # python akan memanggilnya default argumen
        """mengubah panjang dari  """
        inch_to_cm = inch * 2.54
        feet_to_cm = feet * 12 * 2.54
        return inch_to_cm + feet_to_cm
    
    
    print(f'ini konversi dari feet({feet}) ke cm {cm(feet)}')
    print(f'ini konversi dari inch({inch}) ke cm {cm(inch)}')
    print(f'ini gabungan dari feet({feet}) dan inch({inch}) ke cm {cm(feet,inch)}')
    isdone = input('apakah sudah selesai y/n ? ')
    if isdone == 'y':
        break

while(True):
    # contoh type dari argumen        
        print('contoh type dari argumen')
        
        # jika seperti ini akan eror karena non-default argument follow default argument
        # def y(a = 0, b):
        #     return a + b
        # untuk memperbaikinya bisa seperti ini
        def y(a, b = 0): # a adalah argumen yang diperlukan 
            # argumen b adalah opsional bisa diisi atau tidak
            return a + b 
        print(f"ini adlah hasil type argumen {y(9,b=1)}")
        isdone = input('apakah sudah selesai y/n ? ')
        if isdone == 'y':
            break
                