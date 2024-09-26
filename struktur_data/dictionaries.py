# Dictionary adalah kumpulan pasangan key: value, di mana key harus unik dan berupa tipe data yang tidak bisa diubah (immutable), seperti string atau angka. Tipe data seperti tuple juga bisa menjadi key jika semua elemennya immutable. Namun, list tidak dapat digunakan sebagai key karena bisa diubah.

# Operasi utama pada dictionary meliputi menyimpan nilai dengan key, mengambil nilai berdasarkan key, dan menghapus pasangan key: value menggunakan del. Jika key yang sama digunakan untuk menyimpan nilai baru, nilai lama akan ditimpa. Mengakses key yang tidak ada akan menghasilkan error.

# Untuk mendapatkan daftar semua key, dapat menggunakan list(d) yang akan menampilkan urutan sesuai dengan urutan penyisipan. Untuk memeriksa keberadaan key, gunakan kata kunci in.

# contoh
bio = {'nama':'ucup','alamat':'SBY','jurusan':'TKJ'}

# menambahkan dict
bio['negara'] = 'indonesia'

# loop dict
# for key,data in bio.items():
#     print(f'key: {key} value: {data}')

# list komprehension
sets = [[key,value] for key,value in bio.items()]

print(sets)
print(f"bio ucup: {bio}")

# mengubah dict
bio['nama'] = 'abyan'

print(f"bio ucup: {bio}")
# menghapus salah satu dict
del bio['negara']

# print(f"loop dict: {loop}")
print(f"bio ucup: {bio}")

# ambil key pakai list
print(list(bio))

# mengurutkan key
print(sorted(bio))

# cek
isinsets_ = 'nama' in bio
print(f"apakah ada nama di bio: {isinsets_}\n")

# sebuah dict() constructor akan membuat beberapa dictionary secara langsung dari urutan sepasang key-value

# Membuat nested dictionary menggunakan list dari tuples
dict_ = dict([
    ('nama', 'peltod'),
    ('alamat', 'ASIA'),
    ('negara', 'indonesia'),
    ('hoby', dict([
    ('aktif','ngoding'),('pasif', 'turu')]))
]) # atau menggunakan penamaan argumen
dict_name = dict(
    nama='peltod',
    alamat='ASIA',
    negara='Indonesia',
    hoby=dict(
        aktif='ngoding',
        pasif='turu'
    )
)

# for key,value in dict_.items():
#     print(f"key({key}) value({value})")
print(f"dict_name_arg {dict_name}")
print(f"dict: {dict_}")

# membuat dict menggunakan list komprehension
create_dict = {key:value for key,value in dict_name.items()}
print(f'dict: {create_dict}')

