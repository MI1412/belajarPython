# Fungsi **`open()`** mengembalikan objek file dan umumnya digunakan dengan dua argumen posisi dan satu argumen kata kunci: **`open(filename, mode, encoding=None)`**.

# Contoh:
# ```python
# f = open('workfile', 'w', encoding="utf-8")
# ```

# **Penjelasan:**
# - Argumen pertama adalah nama file.
# - Argumen kedua, **`mode`**, adalah string yang menjelaskan bagaimana file akan digunakan. Contoh:
#   - **`'r'`**: hanya untuk membaca.
#   - **`'w'`**: hanya untuk menulis (file yang sudah ada akan dihapus).
#   - **`'a'`**: menambahkan data ke akhir file.
#   - **`'r+'`**: untuk membaca dan menulis.
# - Mode standar adalah **`'r'`** jika mode tidak ditentukan.
# - Mode teks digunakan untuk membaca dan menulis string yang dienkode dalam format tertentu, seperti **UTF-8**. Mode biner (**`'b'`**) digunakan untuk membaca dan menulis data biner seperti objek **bytes**.

# Ketika file dibuka dalam mode teks, **line endings** (\n pada Unix, \r\n pada Windows) otomatis dikonversi ke **\n** saat membaca, dan dikonversi kembali saat menulis. Ini tidak berlaku untuk mode biner. Oleh karena itu, mode biner harus digunakan saat menangani data biner (misalnya gambar JPEG atau file EXE).

# **Praktik Terbaik:**
# - Gunakan kata kunci **`with`** saat bekerja dengan objek file. Ini menjamin file ditutup dengan benar setelah selesai, bahkan jika terjadi pengecualian.
  
# Contoh:
# ```python
# with open('workfile', encoding="utf-8") as f:
#     read_data = f.read()
# ```
# Setelah blok **`with`** selesai, file otomatis ditutup.

# **Peringatan:**
# - Jika tidak menggunakan **`with`**, Anda harus memanggil **`f.close()`** untuk menutup file dan membebaskan sumber daya.
# - Jika **`f.close()`** tidak dipanggil, data yang ditulis dengan **`f.write()`** mungkin tidak tersimpan ke disk secara lengkap, meskipun program selesai dijalankan.

# Jika file sudah ditutup, mencoba mengaksesnya lagi akan menghasilkan kesalahan.

# Contoh kesalahan:
# ```python
# f.close()
# f.read()
# ```
# Akan menghasilkan:
# ```
# ValueError: I/O operation on closed file.
# ```

# **Kesimpulan:**
# - **`open()`** digunakan untuk membuka file dalam mode baca, tulis, atau tambahkan.
# - Mode biner digunakan untuk data non-teks.
# - **`with`** memastikan file selalu ditutup dengan aman.
# - Jika tidak menggunakan **`with`**, selalu panggil **`f.close()`** setelah selesai menggunakan file.

# contoh 
# membuka file
file = open('workfile.txt', mode='w', encoding="utf-8")
print(file)

# membuka dan membaca file
with open('workfile.txt','r', encoding="utf-8") as f:
    read_data = f.read()
    print(f.closed) # menutup file


