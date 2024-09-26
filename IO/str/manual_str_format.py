# disini adalah format dari urutan dan kubus diformat secara manual:
for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')

print(repr(x*x*x).rjust(4))

# Perhatikan bahwa satu spasi antar kolom ditambahkan karena cara kerja fungsi print(), yang secara otomatis menambahkan spasi antara argumennya.

# Metode str.rjust() pada objek string akan meratakan (justify) string ke kanan dalam sebuah kolom dengan lebar tertentu, dan mengisinya dengan spasi di sebelah kiri. Ada juga metode serupa, yaitu str.ljust() dan str.center(), yang meratakan string ke kiri dan tengah. Metode-metode ini tidak mencetak apapun, tetapi mengembalikan string baru. Jika string masukan terlalu panjang, metode ini tidak memotongnya, namun tetap mengembalikan string apa adanya, meskipun ini dapat merusak tata letak kolom. Hal ini dianggap lebih baik daripada memanipulasi nilai sebenarnya. Jika Anda ingin memotong string secara manual, Anda bisa menggunakan operasi slice, seperti pada x.ljust(n)[:n].

# Ada metode lain yaitu str.zfill() yang mengisi string numerik dengan nol di sebelah kiri. Metode ini juga memahami tanda plus dan minus.

# Kesimpulan: Metode str.rjust(), str.ljust(), dan str.center() digunakan untuk merapikan string sesuai lebar kolom dengan penambahan spasi, tanpa mengubah nilai aslinya. Jika ingin memotong string, Anda harus melakukannya sendiri menggunakan operasi slice. Sementara itu, metode str.zfill() digunakan untuk mengisi angka dengan nol di sebelah kiri.

# Contoh:

# <--Menggunakan str.rjust() untuk meratakan ke kanan:
text = 'Hello'
print(f"rata kanan: {text.rjust(10)}") 

# <--Menggunakan str.ljust() untuk meratakan ke kiri:
print(f"rata kiri: {text.ljust(10)}")  # Output: 'Hello     '

# <--Menggunakan str.center() untuk meratakan ke tengah:
print(f"rata tengah: {text.center(10)}")  # Output: '  Hello   '

# <--Menggunakan str.zfill() untuk mengisi angka dengan nol:
number = '42'
print(f"number {number} diisi 000:{number.zfill(5)}")  # Output: '00042'

# 