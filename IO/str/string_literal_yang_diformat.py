# format string literal / f-string
# pada saat print() tambahkan f dan tambahkan {} didalam string:
# {} digunakan untuk menampilkan variabel, fungsi, module, dll
# print(f"string {}")
# contoh
import math
print(f'Nilai pi kira-kira {math.pi:.3f}.')


# menambahkan integer setelah : di tipe data mapping / dictionary, digunakan untuk membuat kolom rapi

mapp = {"nama":1010,"alamat":1010,"id":1010}
for key,value in mapp.items():
    print(f"{key:10} ==> {value:10d}")

# Modifikator lain dapat digunakan untuk mengonversi nilai sebelum diformat. !a menerapkan ascii(), !s menerapkan str(), dan !r menerapkan repr():
binatang = 'eels'
print(f"binatang tanpa !a: {binatang}")
print(f"binatang pakai !a: {binatang!a}")
print(f"binatang pakai !s: {binatang!s}")
print(f"binatang pakai !r: {binatang!r}")

# Specifier = dapat digunakan untuk memperluas ekspresi menjadi teks ekspresi, tanda sama dengan, kemudian representasi ekspresi yang dievaluasi:

serangga = 'roaches'
hitung = 13
area = 'living room'
print(f'Debugging: {serangga=} {hitung=} {area=}')