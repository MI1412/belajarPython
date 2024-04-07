# module mtk dengan import 
# from matematika import tambah,kali,pangkat # memakai = from (nama module) import (function) ini digunakan untuk mendeklair namespace secara global sehingga tidak perlu memanggil ulang namespacenya
# from matematika import * # digunakan untuk mengimport semua funct


# penamaan as atau dalam bahasa inggris sebagai 
# contoh penamaan as di funct didalam module 
from matematika import tambah as add # setelah as bisa ditulis nama module yang sesuai fungsi, kalau dibaca tambah itu sebagai add dalam module matematika 
# contoh penamaan as di nama module
import matematika as math

hasil_tambah = add(1,4,56,8)
print(f"hasil tambah = {hasil_tambah}")
hasil_kali = math.kali(1,4,56,8)
print(f"hasil kali = {hasil_kali}")

pangkat = math.pangkat(4)
print(f"hasil pangkat = {pangkat(2)}")