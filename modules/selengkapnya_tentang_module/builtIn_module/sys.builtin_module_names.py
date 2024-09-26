#  ada sebuah tuple yang berisi nama-nama modul yang telah dikompilasi langsung ke dalam interpreter Python. Berbeda dengan sys.modules.keys(), yang hanya menampilkan modul-modul yang telah diimpor dalam sesi saat ini, tuple ini menampilkan semua modul bawaan (compiled) yang termasuk dalam interpreter Python, termasuk modul yang belum diimpor.

# Poin-poin penting:

# Tuple ini berisi nama modul yang telah dikompilasi ke dalam interpreter Python.
# Ini adalah satu-satunya cara untuk melihat modul-modul tersebut (karena modules.keys() hanya menampilkan modul yang sudah diimpor).
# Ada juga sys.stdlib_module_names, daftar modul pustaka standar Python yang mungkin relevan untuk informasi lebih lanjut.
# Kesimpulannya, dokumentasi ini membedakan antara modul yang dikompilasi ke dalam interpreter dan modul yang diimpor, serta menyoroti bahwa informasi tentang modul yang dikompilasi hanya bisa diakses melalui tuple tersebut.
import sys
print(sys.builtin_module_names)
# Output-nya akan berupa tuple yang berisi nama-nama modul yang sudah dikompilasi, seperti ('_abc', 'array', 'sys', ...).
print(sys.stdlib_module_names)
# lihat penjelassan di sys.stdlib_module_names.py

# Perbedaan:
# sys.builtin_module_names: Menampilkan modul yang built-in ke interpreter.
# sys.stdlib_module_names: Menampilkan modul pustaka standar Python.