# Operator % (modulo) juga bisa digunakan untuk memformat string. Dalam format format % values (di mana format adalah sebuah string), spesifikasi konversi dalam format akan digantikan dengan satu atau lebih elemen dari values. Operasi ini dikenal sebagai interpolasi string.
# Contoh:
import math
print('The value of pi is approximately %5.3f.' % math.pi)
# Dalam contoh di atas, %5.3f menunjukkan bahwa nilai pi akan diformat menjadi angka desimal dengan 3 tempat setelah titik, dan total minimal 5 karakter termasuk angka dan titik desimal.
