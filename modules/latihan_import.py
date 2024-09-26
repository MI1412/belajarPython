from modules import calc # dari module import fungsi ini, cara ini tidak perlu definisi module lagi

tambah = calc(1,'+',4)
print(f"tambah: {tambah}")

from modules import * # mengambil semua isi module, penggunaan metode ini buruk
# akan ambil seluruh isi module kecuali yang dimulai dengan _underscore, praktik ini tidak disarankan karena dapat memperkenalkan banyak nama baru ke environment yang berpotensi menimpa
# _hai('imron')
kurang = calc(9,'-',7)
print(f"kurang {kurang}")

# jika menggunakan as maka akan menamai modul dengan nama lain
import modules as mod
# lebih efektif menggunakan from
from modules import calc as c 

# catatan : jika ingin melakukan mengulangi lagi modul tanpa keluar dari python interpreter
# menggunakan module importlib
import importlib
importlib.reload(mod)
# ini memungkinkan modul dimuat ulang tanpa memulai ulang sesi interpreter

# <--eksekusi beberapa module alias sebagai script
# saat menjalankan module python dengan

import sys

if __name__ == "__main__":
    print(calc(1,'+',9))

# pencarian alamat module

# Ketika sebuah modul, seperti spam, diimpor, Python akan pertama-tama mencari modul bawaan dengan nama tersebut(lihat di sysbuiltinmodule.name.py). Jika tidak ditemukan, Python kemudian akan mencari file spam.py di dalam direktori yang ditentukan oleh variabel sys.path.

# Urutan pencarian modul diatur sebagai berikut:

# Direktori tempat skrip input berada (atau direktori saat ini jika tidak ada file yang spesifik).
# Variabel lingkungan PYTHONPATH (yang berisi daftar direktori dengan sintaks yang sama seperti variabel PATH di shell).
# Direktori default yang bergantung pada instalasi, yang biasanya mencakup direktori site-packages.
# Jika modul masih belum ditemukan, Python akan memberi kesalahan.

# Catatan tambahan:

# Python menghitung direktori skrip setelah symlink diikuti (pada file system yang mendukung symlink), sehingga direktori yang berisi symlink tidak akan ditambahkan ke sys.path.
# Setelah inisialisasi, program Python dapat memodifikasi sys.path. Namun, direktori yang berisi skrip akan berada di awal jalur pencarian, sehingga modul dari direktori itu akan dimuat terlebih dahulu dibandingkan modul dengan nama yang sama di pustaka standar, yang bisa menyebabkan kesalahan jika penggantian tidak diinginkan.

