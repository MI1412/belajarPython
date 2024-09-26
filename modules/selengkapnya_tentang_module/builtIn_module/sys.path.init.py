# ### Penjelasan

# Dokumentasi yang Anda referensikan menjelaskan bagaimana jalur pencarian modul diinisialisasi dan diatur di Python melalui `sys.path`. Berikut adalah langkah-langkah rinci tentang bagaimana `sys.path` dibentuk saat Python mulai berjalan:

# 1. **Inisialisasi Awal:**
#    - **Jika ada skrip yang dijalankan (`python script.py`):** Direktori yang berisi skrip tersebut akan menjadi entri pertama di `sys.path`.
#    - **Jika tidak ada skrip:** Direktori kerja saat ini (current directory) akan menjadi entri pertama di `sys.path`. Ini berlaku untuk shell interaktif, perintah `-c`, atau saat menggunakan opsi `-m`.

# 2. **Variabel Lingkungan `PYTHONPATH`:**
#    - **Pengaruh `PYTHONPATH`:** Jika variabel lingkungan `PYTHONPATH` ada, direktori yang disebutkan di dalamnya akan ditambahkan ke `sys.path`. Namun, `PYTHONPATH` akan mempengaruhi semua versi dan lingkungan Python yang diinstal, jadi hati-hati saat mengaturnya di profil shell atau variabel lingkungan global.

# 3. **Direktori Modul Standar dan Ekstensi:**
#    - **Direktori Modul Standar:** Lokasi modul Python standar serta modul ekstensi yang dibutuhkan oleh modul-modul tersebut. Ekstensi ini bisa berupa file `.pyd` di Windows atau `.so` di platform lain.
#    - **Prefix dan Exec_Prefix:** `prefix` adalah direktori dengan modul Python yang independen dari platform, sedangkan `exec_prefix` adalah direktori dengan modul ekstensi. Lokasi ini ditentukan menggunakan variabel lingkungan `PYTHONHOME` jika ada, atau dengan mencari direktori dan file landmark jika tidak ada.

# 4. **Penentuan Prefix dan Exec_Prefix:**
#    - **`PYTHONHOME`:** Jika ditetapkan, variabel ini menentukan lokasi `prefix` dan `exec_prefix`.
#    - **Penemuan Automatis:** Jika tidak ada `PYTHONHOME`, Python akan mencari `prefix` dan `exec_prefix` mulai dari lokasi eksekusi Python. Ini melibatkan pencarian file zip (misalnya, `python311.zip`) atau direktori `lib`.

# 5. **Pemrosesan Modul `site`:**
#    - **Direktori `site-packages`:** Setelah menemukan `prefix` dan `exec_prefix`, direktori `site-packages` ditambahkan ke `sys.path`.
#    - **Kustomisasi:** Anda dapat menambahkan modul `sitecustomize` atau `usercustomize` untuk menyesuaikan jalur pencarian lebih lanjut.

# 6. **Opsi Baris Perintah:** 
#    - Beberapa opsi baris perintah seperti `-E`, `-I`, `-s`, dan `-S` dapat mempengaruhi perhitungan jalur.

# ### Kesimpulan

# `sys.path` diinisialisasi berdasarkan direktori skrip, direktori kerja saat ini, variabel lingkungan `PYTHONPATH`, dan direktori standar Python. Modifikasi `sys.path` dapat dilakukan dengan menambahkan direktori kustom atau menggunakan modul `sitecustomize`. Variabel lingkungan dan opsi baris perintah juga dapat mempengaruhi jalur pencarian.

# ### Contoh Penggunaan

# 1. **Menjalankan Skrip Python (`python script.py`):**
#    ```python
#    # Jika script.py berada di /home/user/projects/
#    import sys
#    print(sys.path)
#    ```
#    - Output: `/home/user/projects/` akan menjadi entri pertama di `sys.path`.

# 2. **Menambahkan Direktori dengan `PYTHONPATH`:**
#    ```bash
#    export PYTHONPATH=/path/to/my/modules
#    python myscript.py
#    ```
#    - Output: `/path/to/my/modules` akan ditambahkan ke `sys.path`.

# 3. **Menetapkan `PYTHONHOME`:**
#    ```bash
#    export PYTHONHOME=/path/to/python
#    python myscript.py
#    ```
#    - `prefix` dan `exec_prefix` akan diatur berdasarkan `/path/to/python`.

# 4. **Menjalankan Python dengan Opsi `-I`:**
#    ```bash
#    python -I myscript.py
#    ```
#    - Mengabaikan `PYTHONPATH` dan direktori kerja saat ini dari `sys.path`.

# 5. **Modifikasi dengan `sitecustomize`:**
#    ```python
#    # Buat file sitecustomize.py di direktori site-packages
#    # Misalnya: /path/to/site-packages/sitecustomize.py
#    import sys
#    sys.path.append('/custom/path')
#    ```
#    - `/custom/path` akan ditambahkan ke `sys.path` saat Python diinisialisasi.