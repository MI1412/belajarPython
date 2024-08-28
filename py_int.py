# tipe data angka
# int, complex, float, tipe data angka dari bahasa c
from ctypes import c_int
from ctypes import c_float
from ctypes import c_double

isi_int = dir(int)
isi_complex = dir(complex)
isi_float = dir(float)
isi_C_int = dir(c_int())
isi_C_float = dir(c_float())
isi_C_double = dir(c_double())

print(f"isi dari int \n{isi_int}\n")
print(f"isi dari complex \n{isi_complex}\n")
print(f"isi dari float \n{isi_float}\n")
# print(f"isi dari C_int \n{isi_C_int}\n")
# print(f"isi dari C_float \n{isi_C_float}\n")
# print(f"isi dari C_double \n{isi_C_double}\n")

# 1. int
# ada 66 Dunder method
# ada 11 method 
# contoh 
angka_int = 9
angka_pecahan = .75
# print(type(angka_int)) = output int

# as integer ratio digunakan untuk mengubah sebuah pecahan ke bentuk int dengan akurat
as_int_ratio = angka_pecahan.as_integer_ratio()
# help(as_int_ratio)
# as_int_ratio mengembalikan nilai dalam bentuk tuple (p/q) p = penyebut, q = pembilang
# 0.75 = 3/4
print(f"hasil dari rasio {angka_pecahan} dirubah ke int {as_int_ratio}")

# bit lenght menghitung panjang bit dalam angka
angka_int = int(1010)
hitung_angkaKe_bentukbit = angka_int.bit_length()
print(f"ini adalah angka int : {angka_int}")
print(f"bit_lenght() hitung panjang angka int dalam bit : {hitung_angkaKe_bentukbit}")

# conjugate digunakan untuk merasionalkan penyebut dan menghitung modulus
int_conjugate = angka_int.conjugate()
print(int_conjugate)

# 2. complex
# ada 42 Dunder method
# ada 3 method


# 3. float
# ada 53 Dunder method
# ada 7 method


# belum paham C ga dulu
# 4. C_int
# angka_c_int = c_int(1)
# print(angka_c_int)





