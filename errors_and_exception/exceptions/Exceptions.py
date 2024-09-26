# Kesimpulan tentang **Exceptions** di Python:

# Meskipun sebuah pernyataan atau ekspresi secara sintaksis benar, saat dieksekusi mungkin akan menyebabkan kesalahan yang disebut **exceptions**. Exceptions terjadi selama eksekusi program dan dapat diatasi melalui penanganan kesalahan. Namun, jika tidak ditangani, exceptions akan menghasilkan pesan kesalahan.

# Contoh exceptions yang sering terjadi:
# 1. **ZeroDivisionError**: Muncul saat ada pembagian dengan nol.
# #    - Contoh: `10 * (1/0)`
# 2. **NameError**: Terjadi ketika variabel yang belum didefinisikan dipanggil.
#    - Contoh: `4 + spam*3` (di mana `spam` belum didefinisikan)
# 3. **TypeError**: Muncul saat ada operasi yang dilakukan pada tipe data yang tidak kompatibel.
#    - Contoh: `'2' + 2` (tidak bisa menjumlahkan string dengan integer)

# ### Struktur Pesan Error:
# - **Tipe Exception**: Nama exception yang muncul, misalnya: `ZeroDivisionError`, `NameError`, dan `TypeError`.
# - **Detail Kesalahan**: Penjelasan tentang kesalahan yang terjadi.
# - **Stack Traceback**: Bagian awal dari pesan kesalahan yang menunjukkan di mana kesalahan terjadi, sering kali disertai dengan baris kode yang menyebabkan error.

# Exceptions bawaan Python memiliki nama standar dan terintegrasi sebagai **identifiers** (bukan kata kunci yang dipesan).

# ### Kesimpulan:
# Exceptions membantu mengidentifikasi kesalahan spesifik dalam program Python. Mereka memiliki tipe yang bervariasi, dan pesan error memberikan informasi detail yang berguna untuk memperbaiki masalah. Anda bisa menggunakan penanganan exception (misalnya dengan blok `try-except`) untuk mengatasi kesalahan ini dan mencegah program berhenti mendadak.