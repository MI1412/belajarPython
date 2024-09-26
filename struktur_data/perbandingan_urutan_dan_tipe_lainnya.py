# membandingkan objek-objek berjenis urutan (sequence) menggunakan urutan leksikografis. Perbandingan dimulai dari elemen pertama di kedua urutan; jika elemen pertama berbeda, hasil perbandingan ditentukan oleh elemen tersebut. Jika sama, maka perbandingan berlanjut ke elemen berikutnya, dan proses ini terus berlangsung hingga salah satu urutan selesai atau ditemukan perbedaan.

# Jika elemen dalam urutan adalah urutan lain, perbandingan dilakukan secara rekursif dengan aturan yang sama. Jika kedua urutan memiliki elemen yang sama hingga akhir, urutan yang lebih pendek dianggap lebih kecil. Dalam urutan string, perbandingan dilakukan berdasarkan nomor kode Unicode.

# Contoh dari dokumentasi menunjukkan bahwa berbagai tipe urutan (tuple, list, dan string) dapat dibandingkan, bahkan jika urutan tersebut terdiri dari elemen yang lebih kompleks seperti urutan di dalam urutan lainnya. Untuk tipe numerik yang berbeda, perbandingan dilakukan berdasarkan nilai numeriknya.

# contoh perbandingan dengan lexicographical / perbandingan urutan
# 1.tuple
tuple_ = (1, 2, 3) < (1, 2, 4)  # Hasil: True
print(f"compare tuple: {tuple_}")
# Elemen pertama dan kedua sama, tetapi elemen ketiga dari urutan pertama (3) lebih kecil daripada elemen ketiga urutan kedua (4), sehingga urutan pertama lebih kecil.

# 2.list
list_ = 'ABC' < 'C' < 'Pascal' < 'Python'  # Hasil: True
print(f"list: {list_}")
# Perbandingan string menggunakan urutan karakter berdasarkan nilai Unicode. Huruf 'A' memiliki kode Unicode lebih kecil dari 'C', sehingga 'ABC' lebih kecil dari 'C'.

# 3.nested tuple
nested_tuple = (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)  # Hasil: True
# Perbandingan dilakukan secara rekursif. Di elemen ketiga, 'aa' lebih kecil dari 'abc' karena perbandingan leksikografis dari string.
print(f"nested tuple {nested_tuple}")

# 4.numerik campuran
numerik = (1, 2, 3) == (1.0, 2.0, 3.0)  # Hasil: True
# Meskipun tipe data berbeda (integer dan float), nilai numeriknya sama sehingga kedua urutan dianggap setara.
print(f"numerik: {numerik}")