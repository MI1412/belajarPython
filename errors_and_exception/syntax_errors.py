# **Kesalahan Sintaks (Syntax Errors):**

# Kesalahan sintaks atau **parsing errors** adalah salah satu keluhan paling umum yang sering ditemui saat seseorang belajar Python.

# Contoh:
# ```python
# >>> while True print('Hello world')
#   File "<stdin>", line 1
#     while True print('Hello world')
#                ^^^^^
# SyntaxError: invalid syntax
# ```

# - **Penjelasan**: Python akan mengulang baris yang mengandung kesalahan dan menampilkan panah kecil (`^^^^^`) untuk menunjukkan posisi di mana kesalahan terjadi.
# - **Penyebab**: Kesalahan bisa disebabkan oleh kurangnya tanda tertentu sebelum token yang ditunjukkan oleh panah. Dalam contoh ini, kesalahan terjadi di fungsi `print()`, karena ada tanda titik dua (`:`) yang hilang setelah `while True`.
# - **Informasi tambahan**: Python juga mencetak nama file dan nomor baris untuk memudahkan mencari lokasi kesalahan dalam sebuah script.

# **Kesimpulan**: Kesalahan sintaks biasanya terjadi karena aturan penulisan kode yang tidak sesuai, dan Python memberikan petunjuk posisi untuk membantu menemukan kesalahan dengan cepat.