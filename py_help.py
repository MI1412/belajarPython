# fitur help di python digunakan untuk memberi informasi dari method code yang digunakan
# contoh
# isi_dir_builtin = dir(__builtins__)
# print(isi_dir_builtin)
# kita coba salah satu Dunder method yang berisi method zip

# zip digunakan untuk menggabungkan data iterable misal list dengan list, membuat dictionary, membandingkan objek iterable
# iterable = objek yang dapat diubah
# help(zip)
tuple_1 = (range(3))
tuple_2 = ('a','b','c','d')
zipped = zip(tuple_1,tuple_2)
result = tuple(zipped)
print(tuple(result))