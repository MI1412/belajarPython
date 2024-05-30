contoh = set()
print(f'isi dari set : {dir(contoh)}')

# menampilkan cara menggunakan method add
# help(contoh.add)

contoh.add(10)
contoh.add(True)
contoh.add(2.1444)
contoh.add('yayaya')

print(f"\ncontoh dari sets : {contoh}")
print(type(contoh))

# menghitung elemen
print(f'\npanjang elemen : {len(contoh)}')

# menghapus elemen
# help(contoh.remove)
contoh.remove('yayaya')
print(f"\ncontoh dari sets : {contoh}")
print(f'panjang elemen : {len(contoh)}')


# help(contoh.discard)
# discard() akan mengabaikan exception jika tidak ada member terdaftar
contoh.discard(50)
print(f"\ncontoh dari sets : {contoh}")
print(f'panjang elemen : {len(contoh)}')

contoh2 = set([90,'yayaya',True,89,122])
print(f'\ncontoh set kedua : {contoh2}')
print(f"panjang list : {len(contoh2)}")



# menggabungkan angka 1-10
ganjil = set([1,3,5,7,9])
genap = set([2,4,6,8,10])
tambahan = set([2,3,5,7,8,6])
komposisi = set([4,6,8,9,10])

penggabungan = ganjil.union(genap)
# begitu juga sebaliknya genap.union(ganjil)
print(f'\nangka digabung {penggabungan}')
print(f'ganjil : {ganjil}')
print(f'genap : {genap}')

# angka yang ada dari ganjil
angka_yang_ada = ganjil.intersection(tambahan)
# begitu juga sebaliknya genap.intersection(tambahan)
print(f'angka yang ada {angka_yang_ada}')

# maka akan menampilkan hasil none 
print('\n',genap.intersection(ganjil))

angka_digabung = tambahan.union(komposisi)
print(f'angka digabung {angka_digabung}')

# bisa menghasilkan nilai boolean
apkh_ini_genap = 2 in tambahan
apkh_ini_ganjil = 2 in ganjil
print(f'apakah 2 ada didalam var tambahan {apkh_ini_genap}')
print(f'apakah 2 ada didalam ganjil {apkh_ini_ganjil}')

bukan_dari_genap = 9 not in genap
print(f'9 bukan dari genap : {bukan_dari_genap} ')
bukan_dari_ganjil = 8 not in ganjil
print(f'8 bukan dari ganjil : {bukan_dari_ganjil}')


