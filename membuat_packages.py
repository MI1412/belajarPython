# packages digunakan untuk tempat menaruh module
import time
t_start = time.time()

import sains.matematika
from sains import fisika
from sains.fisika import gaya

hasil_tambah = sains.matematika.tambah(12,78,7)
print(f"\nhasil tambah \t\t: {hasil_tambah}")

t_end = time.time()

print(f"waktu eksekusi adalah \t: {t_end - t_start} ") # untuk menghitung berapa lama waktu eksekusi yang didalamnya ada pycache

hasil_gaya = fisika.gaya(90,10)

print(f"gaya adalah {hasil_gaya}")

hasil_gaya = gaya(9,10)

print(f"gaya adalah {hasil_gaya}")
