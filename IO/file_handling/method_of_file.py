# **Terjemahan dan Kesimpulan:**

# Untuk membaca isi file, kita bisa menggunakan metode **`f.read(size)`** yang akan membaca sejumlah data dan mengembalikannya sebagai string (dalam mode teks) atau bytes (dalam mode biner). **`size`** adalah argumen opsional yang menunjukkan jumlah data yang ingin dibaca. Jika **`size`** tidak diisi atau bernilai negatif, maka seluruh isi file akan dibaca. Jika akhir file telah tercapai, **`f.read()`** akan mengembalikan string kosong (`''`).

# - **`f.readline()`** membaca satu baris dari file dan meninggalkan karakter **`\n`** di akhir string, kecuali jika file tidak diakhiri dengan **newline**. 
# - Untuk membaca file baris demi baris, kita bisa menggunakan perulangan **for** yang efisien dalam hal memori dan cepat.

# Contoh:

f = open('workfile.txt', 'w', encoding="utf-8")

# for line in f:
#     print(line, end='')

# - Jika ingin membaca semua baris sekaligus, bisa menggunakan **`list(f)`** atau **`f.readlines()`**.
  
# Untuk menulis ke dalam file, gunakan **`f.write(string)`**. Metode ini mengembalikan jumlah karakter yang ditulis.

# Contoh:

f.write('This is a test\n')

# Objek lain seperti tuple harus dikonversi ke string terlebih dahulu sebelum ditulis.

# Contoh:

value = ('the answer', 42)
s = str(value)
f.write(s)

# Metode **`f.tell()`** mengembalikan posisi file saat ini, dihitung dari awal file. Untuk mengubah posisi file, gunakan **`f.seek(offset, whence)`** di mana **`offset`** adalah pergeseran posisi dan **`whence`** adalah titik referensi (awal file, posisi saat ini, atau akhir file).

# Contoh:

f.seek(5)  # Pergi ke byte ke-6
f.read(1)  # Membaca byte tersebut


# Dalam file teks, hanya pergeseran relatif dari awal file yang diperbolehkan, kecuali jika ingin menggeser ke akhir file dengan **`seek(0, 2)`**.

# **Kesimpulan:**
# - **`f.read()`** membaca data dari file.
# - **`f.readline()`** membaca satu baris dari file.
# - **`f.write()`** menulis data ke dalam file.
# - **`f.tell()`** dan **`f.seek()`** digunakan untuk mengetahui dan mengubah posisi dalam file.
# - Metode ini umum digunakan untuk pengelolaan file, namun metode lain seperti **`isatty()`** dan **`truncate()`** lebih jarang dipakai.