t = 12345, 'str', True
print(f"t[0]: {t}")
print(f"t[0]: {t[1]}")

tambah = t, (1,2,3,4,5)

print(f"tambah item tuple {tambah}")
# tuple bersifat immutable / tetap
# print(f"diubah tuple {t}")
# tetapi mereka bisa mengubah objeknya
x = ([1, 2, 3], [3, 2, 1])
print(f"x: {x}")

# tuple selalu ditandakan dengan ()
# gunakan tanda kurung didalam tanda kurung (()) untuk membuat tuple bersarang
# Masalah khusus adalah pembuatan tuple yang berisi 0 atau 1 item: sintaksisnya memiliki beberapa keanehan tambahan untuk menyesuaikan ini. Tuple kosong dibuat dengan pasangan tanda kurung kosong; tuple dengan satu item dibuat dengan mengikuti nilai dengan tanda koma (tidak cukup hanya menempatkan nilai tunggal dalam tanda kurung). Tidak cantik, tetapi efektif. Sebagai contoh:
tuple_kosong = ()
singleton = 'hello',
print(f"panjang tuple kosong {len(tuple_kosong)}")
print(f"panjang singleton: {len(singleton)}")
print(f"singleton {singleton}")

t = 12345, 54321, 'hello!' # contoh statement tuple packing
# sama seperti x,y,z = t