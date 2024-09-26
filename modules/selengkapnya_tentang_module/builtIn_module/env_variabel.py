# Teks tersebut menjelaskan berbagai variabel lingkungan (environment variables) yang dapat mempengaruhi perilaku Python. Variabel ini diproses sebelum opsi baris perintah (command-line switches), kecuali untuk opsi `-E` dan `-I`. Secara umum, jika ada konflik antara variabel lingkungan dan opsi baris perintah, opsi baris perintah akan mengesampingkan variabel lingkungan.

# Berikut adalah penjelasan dan contoh penggunaan untuk setiap variabel lingkungan yang disebutkan:

# 1. **PYTHONHOME**
#    - **Fungsi:** Mengubah lokasi pustaka Python standar.
#    - **Contoh:** 
#      ```bash
#      export PYTHONHOME=/my/custom/python
#      ```
#      Ini akan mengubah lokasi pustaka Python dari default ke `/my/custom/python`.

# 2. **PYTHONPATH**
#    - **Fungsi:** Menambah path pencarian modul Python.
#    - **Contoh:** 
#      ```bash
#      export PYTHONPATH=/my/custom/path:/another/path
#      ```
#      Ini akan menambahkan `/my/custom/path` dan `/another/path` ke jalur pencarian modul Python.

# 3. **PYTHONSAFEPATH**
#    - **Fungsi:** Mencegah penambahan path yang tidak aman ke `sys.path`.
#    - **Contoh:** 
#      ```bash
#      export PYTHONSAFEPATH=1
#      ```

# 4. **PYTHONPLATLIBDIR**
#    - **Fungsi:** Mengganti nilai `sys.platlibdir`.
#    - **Contoh:** 
#      ```bash
#      export PYTHONPLATLIBDIR=/my/platlib
#      ```

# 5. **PYTHONSTARTUP**
#    - **Fungsi:** Menentukan file yang dijalankan sebelum prompt interaktif ditampilkan.
#    - **Contoh:** 
#      ```bash
#      export PYTHONSTARTUP=/my/startup.py
#      ```

# 6. **PYTHONOPTIMIZE**
#    - **Fungsi:** Mengaktifkan mode optimasi.
#    - **Contoh:** 
#      ```bash
#      export PYTHONOPTIMIZE=1
#      ```

# 7. **PYTHONBREAKPOINT**
#    - **Fungsi:** Menentukan callable untuk breakpoint default.
#    - **Contoh:** 
#      ```bash
#      export PYTHONBREAKPOINT=mymodule.myfunction
#      ```

# 8. **PYTHONDEBUG**
#    - **Fungsi:** Mengaktifkan mode debug.
#    - **Contoh:** 
#      ```bash
#      export PYTHONDEBUG=1
#      ```

# 9. **PYTHONINSPECT**
#    - **Fungsi:** Mengaktifkan mode inspeksi setelah eksekusi.
#    - **Contoh:** 
#      ```bash
#      export PYTHONINSPECT=1
#      ```

# 10. **PYTHONUNBUFFERED**
#     - **Fungsi:** Menonaktifkan buffering output.
#     - **Contoh:** 
#       ```bash
#       export PYTHONUNBUFFERED=1
#       ```

# 11. **PYTHONVERBOSE**
#     - **Fungsi:** Mengaktifkan output verbose.
#     - **Contoh:** 
#       ```bash
#       export PYTHONVERBOSE=1
#       ```

# 12. **PYTHONCASEOK**
#     - **Fungsi:** Mengabaikan case sensitivity dalam import statements.
#     - **Contoh:** 
#       ```bash
#       export PYTHONCASEOK=1
#       ```

# 13. **PYTHONDONTWRITEBYTECODE**
#     - **Fungsi:** Mencegah penulisan file .pyc.
#     - **Contoh:** 
#       ```bash
#       export PYTHONDONTWRITEBYTECODE=1
#       ```

# 14. **PYTHONPYCACHEPREFIX**
#     - **Fungsi:** Menentukan direktori untuk file .pyc.
#     - **Contoh:** 
#       ```bash
#       export PYTHONPYCACHEPREFIX=/my/pycache
#       ```

# 15. **PYTHONHASHSEED**
#     - **Fungsi:** Menentukan seed untuk hashing.
#     - **Contoh:** 
#       ```bash
#       export PYTHONHASHSEED=42
#       ```

# 16. **PYTHONINTMAXSTRDIGITS**
#     - **Fungsi:** Mengonfigurasi batas panjang string konversi integer.
#     - **Contoh:** 
#       ```bash
#       export PYTHONINTMAXSTRDIGITS=1000
#       ```

# 17. **PYTHONIOENCODING**
#     - **Fungsi:** Mengatur encoding untuk stdin/stdout/stderr.
#     - **Contoh:** 
#       ```bash
#       export PYTHONIOENCODING=utf-8
#       ```

# 18. **PYTHONNOUSERSITE**
#     - **Fungsi:** Mencegah penambahan direktori site-packages pengguna.
#     - **Contoh:** 
#       ```bash
#       export PYTHONNOUSERSITE=1
#       ```

# 19. **PYTHONUSERBASE**
#     - **Fungsi:** Menentukan direktori dasar pengguna.
#     - **Contoh:** 
#       ```bash
#       export PYTHONUSERBASE=/my/userbase
#       ```

# 20. **PYTHONEXECUTABLE**
#     - **Fungsi:** Menentukan nilai `sys.argv[0]` di macOS.
#     - **Contoh:** 
#       ```bash
#       export PYTHONEXECUTABLE=/my/python
#       ```

# 21. **PYTHONWARNINGS**
#     - **Fungsi:** Mengatur perilaku peringatan.
#     - **Contoh:** 
#       ```bash
#       export PYTHONWARNINGS=ignore
#       ```

# 22. **PYTHONFAULTHANDLER**
#     - **Fungsi:** Mengaktifkan faulthandler untuk dump traceback.
#     - **Contoh:** 
#       ```bash
#       export PYTHONFAULTHANDLER=1
#       ```

# 23. **PYTHONTRACEMALLOC**
#     - **Fungsi:** Memulai pelacakan alokasi memori.
#     - **Contoh:** 
#       ```bash
#       export PYTHONTRACEMALLOC=10
#       ```

# 24. **PYTHONPROFILEIMPORTTIME**
#     - **Fungsi:** Menampilkan waktu impor modul.
#     - **Contoh:** 
#       ```bash
#       export PYTHONPROFILEIMPORTTIME=1
#       ```

# 25. **PYTHONASYNCIODEBUG**
#     - **Fungsi:** Mengaktifkan mode debug asyncio.
#     - **Contoh:** 
#       ```bash
#       export PYTHONASYNCIODEBUG=1
#       ```

# 26. **PYTHONMALLOC**
#     - **Fungsi:** Mengatur allocator memori Python.
#     - **Contoh:** 
#       ```bash
#       export PYTHONMALLOC=pymalloc
#       ```

# 27. **PYTHONMALLOCSTATS**
#     - **Fungsi:** Menampilkan statistik allocator pymalloc.
#     - **Contoh:** 
#       ```bash
#       export PYTHONMALLOCSTATS=1
#       ```

# 28. **PYTHONLEGACYWINDOWSFSENCODING**
#     - **Fungsi:** Mengatur encoding sistem file di Windows.
#     - **Contoh:** 
#       ```bash
#       export PYTHONLEGACYWINDOWSFSENCODING=1
#       ```

# 29. **PYTHONLEGACYWINDOWSSTDIO**
#     - **Fungsi:** Menggunakan mode encoding lama untuk konsol di Windows.
#     - **Contoh:** 
#       ```bash
#       export PYTHONLEGACYWINDOWSSTDIO=1
#       ```

# 30. **PYTHONCOERCECLOCALE**
#     - **Fungsi:** Menonaktifkan pemaksaan locale menjadi UTF-8.
#     - **Contoh:** 
#       ```bash
#       export PYTHONCOERCECLOCALE=0
#       ```

# 31. **PYTHONDEVMODE**
#     - **Fungsi:** Mengaktifkan mode pengembangan Python.
#     - **Contoh:** 
#       ```bash
#       export PYTHONDEVMODE=1
#       ```

# 32. **PYTHONUTF8**
#     - **Fungsi:** Mengaktifkan mode UTF-8 Python.
#     - **Contoh:** 
#       ```bash
#       export PYTHONUTF8=1
#       ```

# 33. **PYTHONWARNDEFAULTENCODING**
#     - **Fungsi:** Mengeluarkan peringatan tentang encoding default locale.
#     - **Contoh:** 
#       ```bash
#       export PYTHONWARNDEFAULTENCODING=1
#       ```

# 34. **PYTHONNODEBUGRANGES**
#     - **Fungsi:** Menonaktifkan informasi lokasi tambahan dalam objek kode.
#     - **Contoh:** 
#       ```bash
#       export PYTHONNODEBUGRANGES=1
#       ```

# 35. **PYTHONPERFSUPPORT**
#     - **Fungsi:** Mengaktifkan dukungan untuk profiler Linux perf.
#     - **Contoh:** 
#       ```bash
#       export PYTHONPERFSUPPORT=1
#       ```

# **Kesimpulan:** Variabel lingkungan ini memberikan kontrol yang kuat atas berbagai aspek konfigurasi dan perilaku runtime Python. Dengan mengatur variabel-variabel ini, pengguna dapat menyesuaikan lingkungan Python mereka untuk berbagai keperluan pengembangan dan debugging.