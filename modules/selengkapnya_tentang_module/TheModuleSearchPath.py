# ### Penjelasan

# Ketika Python mengimpor modul, interpreter mengikuti urutan pencarian tertentu untuk menemukan modul yang dimaksud. Berikut adalah langkah-langkah pencarian dan bagaimana `sys.path` berperan dalam proses tersebut:

# 1. **Pencarian Modul Built-in:**
#    - Python pertama kali mencari modul built-in yang sesuai dengan nama modul yang diimpor. Modul-modul built-in ini terdaftar dalam `sys.builtin_module_names`.

# 2. **Pencarian File Modul:**
#    - Jika modul tidak ditemukan sebagai modul built-in, Python kemudian mencari file dengan nama modul (misalnya `spam.py`) di direktori-direktori yang terdaftar dalam `sys.path`.

# 3. **Inisialisasi `sys.path`:**
#    - **Direktori Skrip:** Direktori tempat skrip input berada (atau direktori kerja saat ini jika tidak ada file yang ditentukan) ditambahkan ke `sys.path`.
#    - **Variabel Lingkungan `PYTHONPATH`:** Daftar direktori yang disebutkan dalam `PYTHONPATH` ditambahkan ke `sys.path`.
#    - **Default Instalasi:** Jalur default yang bergantung pada instalasi Python, biasanya termasuk direktori `site-packages`, juga ditambahkan ke `sys.path`.

# 4. **Perhitungan Direktori Skrip:**
#    - Pada sistem file yang mendukung symlink, direktori yang berisi skrip dihitung setelah mengikuti symlink. Artinya, direktori yang berisi symlink tidak ditambahkan ke jalur pencarian modul.

# 5. **Modifikasi `sys.path`:**
#    - Setelah inisialisasi, program Python dapat memodifikasi `sys.path`. Direktori tempat skrip yang sedang dijalankan ditempatkan di awal jalur pencarian, sehingga modul di direktori tersebut akan dimuat terlebih dahulu dibandingkan modul dengan nama yang sama dari direktori standar.

# ### Kesimpulan

# - **Pencarian Modul:** Python mencari modul dengan urutan pencarian yang dimulai dari modul built-in, kemudian file modul di direktori `sys.path`.
# - **Inisialisasi `sys.path`:** `sys.path` diinisialisasi dengan direktori skrip, `PYTHONPATH`, dan jalur default instalasi.
# - **Modifikasi `sys.path`:** Program dapat memodifikasi `sys.path`, dan direktori skrip akan ditempatkan di awal jalur pencarian, memungkinkan skrip lokal menggantikan modul dengan nama yang sama dari pustaka standar.

# ### Contoh Penggunaan

# 1. **Pencarian Modul Built-in:**
#    ```python
#    import sys
#    print(sys.builtin_module_names)
#    ```
#    - Output: Menampilkan tuple dengan nama-nama modul built-in, seperti `('_io', '_pickle', 'builtins', ...)`.

# 2. **Pencarian Modul di `sys.path`:**
#    ```python
#    import sys
#    sys.path.append('/path/to/my/modules')
#    import spam
#    ```
#    - Jika `spam.py` berada di `/path/to/my/modules`, maka modul tersebut akan diimpor dari direktori tersebut.

# 3. **Modifikasi `sys.path`:**
#    ```python
#    import sys
#    sys.path.append('/custom/path')
#    import spam
#    ```
#    - Menambahkan `/custom/path` ke `sys.path`, sehingga Python akan mencari `spam.py` di `/custom/path` terlebih dahulu sebelum mencari di lokasi lain.

# 4. **Pengaruh `PYTHONPATH`:**
#    ```bash
#    export PYTHONPATH=/path/to/additional/modules
#    python myscript.py
#    ```
#    - Jika `spam.py` ada di `/path/to/additional/modules`, maka direktori ini akan dimasukkan ke `sys.path`, memungkinkan modul di direktori tersebut untuk diimpor.

# 5. **Symlink dan Direktori Skrip:**
#    ```bash
#    ln -s /real/path/to/scripts /symlink/path
#    python /symlink/path/myscript.py
#    ```
#    - Python akan mengikuti symlink `/symlink/path` dan menambahkan `/real/path/to/scripts` ke `sys.path` jika skrip tersebut dijalankan dari lokasi symlink.

# 6. **Penggantian Modul Lokal:**
#    ```python
#    # Misalkan ada file spam.py di direktori kerja saat ini
#    import spam
#    ```
#    - Jika ada `spam.py` di direktori kerja saat ini, modul tersebut akan dimuat dan digunakan daripada modul `spam` yang ada di direktori standar, jika modul tersebut dengan nama yang sama ada di direktori standar.