# Berikut adalah terjemahan dan kesimpulan dari halaman tutorial Python tentang pemformatan output:

# ### Terjemahan

# **Pemformatan Output yang Lebih Canggih**

# Modul `str` dan `format` di Python menyediakan cara yang lebih canggih untuk memformat string. Python mendukung pemformatan string menggunakan metode format string, yang memungkinkan Anda untuk menyusun string yang kompleks dengan cara yang lebih elegan dan fleksibel.

# **Fitur Utama:**
# 1. **Placeholder Format:** Anda dapat menggunakan placeholder `{}` dalam string dan menggantinya dengan nilai variabel menggunakan metode `format()`. Misalnya:
#    ```python
#    "{} {}".format("Hello", "World")
#    ```
#    Ini akan menghasilkan string `"Hello World"`.

# 2. **Posisi dan Nama Argumen:** Anda dapat menentukan urutan argumen atau menggunakan nama untuk meningkatkan kejelasan. Misalnya:
#    ```python
#    "{1} {0}".format("World", "Hello")
#    ```
#    Ini akan menghasilkan string `"Hello World"`.

# 3. **Pemformatan Tipe Data:** Anda dapat mengatur cara data ditampilkan, seperti mengatur jumlah desimal, lebar field, atau format angka. Misalnya:
#    ```python
#    "{:.2f}".format(3.14159)
#    ```
#    Ini akan menghasilkan string `"3.14"`.

# 4. **F-strings:** Sejak Python 3.6, f-strings (format string literals) diperkenalkan. Mereka memberikan cara yang lebih ringkas dan efisien untuk melakukan pemformatan string. Contohnya:
#    ```python
#    name = "World"
#    f"Hello {name}"
#    ```
#    Ini akan menghasilkan string `"Hello World"`.

# 5. **Contoh Lebih Lanjut:** Anda dapat melakukan pemformatan lebih kompleks, termasuk penggunaan ekspresi dalam f-strings, format komposit yang kompleks, dan banyak lagi.

# 6. ada fungsi repr() digunakan untuk menghapus format string pada saat output
halo = "halo dunia\n"
print(repr(halo))
print(halo)

# ### Kesimpulan

# Pemformatan output di Python dapat dilakukan dengan berbagai cara yang canggih menggunakan metode `format()` dan f-strings. Metode `format()` memungkinkan penggunaan placeholder dan pemformatan tipe data yang fleksibel, sedangkan f-strings menawarkan cara yang lebih ringkas dan efisien untuk memformat string mulai dari Python 3.6. Kedua metode ini mempermudah pembuatan string yang kompleks dan terformat dengan baik.

