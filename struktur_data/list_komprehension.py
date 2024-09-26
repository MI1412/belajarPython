# list komprehension semacam pembuatan list secara singkat
# hasil operasi list komprehension akan menghasilkan urutan pengulangan atau membuat urutan bersarang tergantung dari kondisi
# didalam [data for data in list atau if kondisi] 

# contoh lengkp
pangkat = []
for data in range(10):
    pangkat.append(data**2)

print(f"pangkat: {pangkat}") 

# atau
pangkat = list(map(lambda x: x**2, range(10)))
print(f"list: {pangkat}")

# list komprehension
list1 = [1,2,3]
list3 = [7,8,9]
list2 = [4,5,6]
list_komprehension = [(x,y,z) for x in list1 for y in list2 for z in list3 if x != y if x!=y]
print(f"list komprehension {list_komprehension}")

# dan itu sama seperti
urutankecil = []
for x in list1:
    for y in list2:
        for z in list3:
            urutankecil.append((x,y,z))

print(f"sub urutan {urutankecil}")


# <--operasi di list komprehension
vect = [-4,-3,-2,-1,0,1,2,3,4]
kali_vect = [x*2 for x in vect]
print(f"kali 2 vector {kali_vect}")

# <--filter
cari_negatif = [x for x in vect if x <0]
cari_positif = [x for x in vect if x >0]
print(f"negatif {cari_negatif}")
print(f"positif {cari_positif}")

# <--memakai function di list komprehension
list_abs = [abs(x) for x in vect]
print(f"abs: {list_abs}")

# <--memanggil satu method untuk semua elemen
buah = ['    mangga','     apel','    alpukat']
potong_buah = [potong.strip() for potong in buah]
print(f"buah {buah}")
print(f"potong buah: {potong_buah}")

# <--membuat satu list dari 2 tuple seperti (angka, mirip)
pangkat_dua = [(x, x**2) for x in range(6) if x!=0]
print(f"angka pangkat dua {pangkat_dua}")

# jika mencoba tanpa kurung akan eror
# pangkat_dua_eror = [x, x**2 for x in range(6) if x!=0]
# print(f"pangkat: {pangkat_dua_eror}")

# <--meratakan list dari beberapa daftar list
vect = [[1,2,3],[4,5,6],[7,8,9]]
ratakan1 = [angka for elem in vect for angka in elem]

print(f"meratakan list: {ratakan1}")


# <--list komprehension bisa berisi expressi yang komplex dan function bercabang
from math import pi
lingkaran = [str(round(pi,i)) for i in range(1,6)]
print(f"lingkaran: {lingkaran}")

# list komprehension bercabang
matrix = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]

# <--mengubah list bercabang menjadi urutan baris dan kolom
matrix_tabel = [[row[i] for row in matrix] for i in range(5) ]
print(f"tabel matrix {matrix_tabel}")

# contoh diatas sama seperti ini
tabel = []
for i in range(5):
    tabel.append([row[i] for row in matrix])

print(f"tabel: {tabel}")

# lebih ringkas menggunakan function zip
tabel_list = list(zip(*matrix))
print(f"tabel list: {tabel_list}")

