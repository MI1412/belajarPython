import packages
import sains
from sains import matematika
# _init_ adalah satu file yang ada didalam pada packages untuk menambahkan fungsi di masing masing file dalam packages

# contoh

hasil_tambah = matematika.tambah(8,99,9)
print(f"\nhasil tambah = {hasil_tambah}")
pangkat = matematika.pangkat(2)
print(f"\nhasil pangkat 2 = {pangkat(2)}")

hasil_kali = sains.kali(1,9)
print(f"\nhasil kali = {hasil_kali}")
hasil_fisika = sains.fisika.gaya(8,9)
print(f"\nhasil fisika = {hasil_fisika}")

# from sains import *  # ini tidak disarankan!!

# hasil_tambah = matematika.tambah(8,99,9)
# print(f"\nhasil tambah = {hasil_tambah}")
# pangkat = matematika.pangkat(2)
# print(f"\nhasil pangkat 2 = {pangkat(2)}")

# hasil_kali = matematika.kali(1,9)
# print(f"\nhasil kali = {hasil_kali}")
# hasil_fisika = fisika.gaya(8,9)
# print(f"\nhasil fisika = {hasil_fisika}")

# pertanyaan kenapa from package import * tidak disarankan dalam import module menggunakan __all__[list module]