# ### Terjemahan

# **Input dan Output di Python**

# Pada Python, ada beberapa cara untuk melakukan input dan output data. Berikut adalah ringkasan dari cara-cara tersebut:

# 1. **Fungsi `print()`**
#    - Digunakan untuk menampilkan output ke layar.
#    - Contoh: `print("Hello, World!")` akan menampilkan teks "Hello, World!" ke layar.

# 2. **Fungsi `input()`**
#    - Digunakan untuk membaca input dari pengguna.
#    - Input yang diberikan oleh pengguna selalu berupa string.
#    - Contoh: `name = input("Enter your name: ")` akan meminta pengguna memasukkan nama mereka, yang kemudian disimpan dalam variabel `name`.

# 3. **Format String**
#    - Ada beberapa cara untuk memformat string di Python:
#      - **Penggabungan String**: Menggunakan operator `+` untuk menggabungkan string.
#      - **Metode `.format()`**: Menyisipkan nilai ke dalam string menggunakan `{}` sebagai placeholder.
#      - **F-strings (format string literals)**: Menggunakan prefiks `f` dan `{}` untuk menyisipkan nilai dalam string. Ini adalah metode terbaru dan paling efisien.

# 4. **File I/O**
#    - Membaca dan menulis data ke file dilakukan dengan menggunakan fungsi bawaan Python seperti `open()`.
#    - File dapat dibuka dalam mode baca (`'r'`), tulis (`'w'`), atau tambahkan (`'a'`).
#    - Contoh: 
#      ```python
#      with open('file.txt', 'w') as file:
#          file.write("Hello, World!")
#      ```

# ### Kesimpulan

# Di Python, input dan output data dapat dilakukan menggunakan fungsi `print()` untuk menampilkan data ke layar dan `input()` untuk membaca data dari pengguna. Data dapat diformat menggunakan berbagai metode, termasuk penggabungan string, metode `.format()`, dan f-strings. Untuk operasi file, Python menyediakan fungsi `open()` untuk membaca dan menulis data ke file dengan berbagai mode akses.
