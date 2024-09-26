# sys.builtin_module_names, yang merupakan frozenset (set yang tidak dapat diubah) yang berisi nama-nama modul standar dari pustaka Python. Ini mencakup berbagai jenis modul, seperti:

# Modul Python murni
# Modul bawaan (built-in)
# Modul beku (frozen)
# Modul ekstensi
# Modul yang tidak tersedia di beberapa platform atau yang dinonaktifkan dalam build Python juga termasuk dalam daftar ini. Namun, modul uji tidak disertakan, dan untuk paket, hanya paket utama yang dicantumkan, bukan sub-paket atau sub-modul.

# Contoh Penggunaan:

# Berikut adalah contoh penggunaan sys.builtin_module_names untuk melihat nama-nama modul standar yang disediakan oleh pustaka Python:

import sys

# Menampilkan semua nama modul standar yang ada
print(sys.builtin_module_names)
# Output dari kode ini akan memberikan frozenset yang berisi nama-nama modul standar yang tersedia di lingkungan Python Anda, misalnya:
# frozenset({'_ast', '_json', '_operator', '_pickle', '_socket', 'builtins', 'fcntl', 'itertools', 'marshal', 'posix', 'sys', 'time'})

# ditambahkan di versi 3.10