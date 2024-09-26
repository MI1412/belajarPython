# ### Penjelasan

# Dokumentasi yang Anda referensikan menjelaskan beberapa hal tentang modul standar di Python, termasuk modul built-in dan cara modul tersebut digunakan. Berikut adalah penjelasan tentang berbagai poin yang dibahas:

# 1. **Modul Standar:**
#    - Python dilengkapi dengan pustaka modul standar yang mendukung berbagai fungsi dan operasi. Modul-modul ini dijelaskan dalam dokumen terpisah, yaitu **Python Library Reference**.
#    - Beberapa modul adalah modul built-in, yang berarti mereka disertakan langsung dalam interpreter Python dan memberikan akses ke operasi yang tidak termasuk dalam inti bahasa tetapi diperlukan untuk efisiensi atau akses ke primitif sistem operasi seperti panggilan sistem.

# 2. **Modul Built-in:**
#    - Modul-modul built-in adalah bagian dari konfigurasi interpreter Python dan mungkin berbeda tergantung pada platform yang digunakan. Misalnya, modul `winreg` hanya tersedia di sistem Windows.
#    - Salah satu modul built-in yang penting adalah `sys`. Modul ini menyediakan akses ke beberapa variabel dan fungsi yang penting untuk pengelolaan lingkungan Python.

# 3. **Variabel `sys.ps1` dan `sys.ps2`:**
#    - `sys.ps1` dan `sys.ps2` adalah variabel yang digunakan untuk mendefinisikan string yang muncul sebagai prompt utama dan prompt sekunder di mode interaktif Python.
#    - **`sys.ps1`**: Prompt utama (misalnya, `>>> `).
#    - **`sys.ps2`**: Prompt sekunder (misalnya, `... `).
#    - Variabel-variabel ini hanya didefinisikan jika interpreter berada dalam mode interaktif.

# 4. **Variabel `sys.path`:**
#    - `sys.path` adalah daftar string yang menentukan jalur pencarian interpreter untuk modul. Jalur ini diinisialisasi dari variabel lingkungan `PYTHONPATH` atau jalur default bawaan jika `PYTHONPATH` tidak diatur.
#    - Anda dapat memodifikasi `sys.path` menggunakan operasi daftar standar, seperti menambahkan direktori ke dalamnya.

# ### Kesimpulan

# - **Modul Standar:** Python menyediakan pustaka modul standar yang meliputi modul built-in dan modul yang diakses melalui variabel lingkungan dan jalur default.
# - **Modul Built-in:** Beberapa modul built-in tersedia secara langsung dalam interpreter Python dan memberikan akses ke operasi penting. Contoh modul built-in termasuk `sys`.
# - **Prompt Interaktif:** Variabel `sys.ps1` dan `sys.ps2` digunakan untuk mengubah tampilan prompt di mode interaktif Python.
# - **Jalur Pencarian Modul:** `sys.path` menentukan jalur pencarian untuk modul, dan dapat dimodifikasi untuk menambahkan direktori baru.

# ### Contoh Penggunaan

# 1. **Mengakses dan Mengubah Prompt Interaktif:**
#    ```python
#    import sys
#    print(sys.ps1)  # Output: '>>> '
#    print(sys.ps2)  # Output: '... '
   
#    sys.ps1 = 'C> '
#    sys.ps2 = '...> '
   
#    # Pada mode interaktif, prompt sekarang akan menjadi 'C> ' dan '...> '
#    ```

# 2. **Menambahkan Direktori ke `sys.path`:**
#    ```python
#    import sys
#    sys.path.append('/ufs/guido/lib/python')
   
#    # Sekarang Python akan mencari modul di direktori '/ufs/guido/lib/python' jika tidak ditemukan di lokasi lain.
#    ```

# 3. **Modul Built-in `sys`:**
#    ```python
#    import sys
#    print(sys.version)  # Menampilkan versi Python yang digunakan
#    print(sys.platform) # Menampilkan platform yang digunakan (misalnya, 'win32', 'darwin', 'linux')
#    ```

# 4. **Menggunakan Variabel Lingkungan `PYTHONPATH`:**
#    ```bash
#    export PYTHONPATH=/path/to/additional/modules
#    python myscript.py
#    ```
#    - Dengan mengatur `PYTHONPATH`, direktori `/path/to/additional/modules` akan ditambahkan ke `sys.path` sehingga modul yang berada di dalamnya dapat diimpor.
