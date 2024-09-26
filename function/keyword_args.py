# <--arguments

# dalam pemanggilan argumen ada dua jenis

# 1. keyword argument
# Keyword argument adalah argumen yang didahului oleh sebuah pengenal (misalnya name=) dalam pemanggilan fungsi, atau diteruskan sebagai nilai dalam sebuah kamus (dictionary) dengan tanda ** di depannya. Dengan keyword arguments, Anda dapat menetapkan nilai argumen berdasarkan nama parameternya, bukan hanya berdasarkan urutannya dalam daftar parameter.
print(complex(real=3, imag=5))

# menggunakan ** untuk meneruskan iterable
print(complex(**{'real': 3, 'imag': 5}))

# 2. positional argumen
# Argumen posisi adalah argumen yang diteruskan ke sebuah fungsi berdasarkan urutan posisinya dalam daftar parameter fungsi. Argumen ini tidak memiliki nama keyword (atau keyword) saat diteruskan. Berbeda dengan argumen kata kunci, argumen posisi dicocokkan dengan parameter fungsi berdasarkan urutannya.
print(complex(3, 5))

# menggunakan * untuk meneruskan iterable
print(complex(*(3, 5)))

