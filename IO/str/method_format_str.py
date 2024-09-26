# penggunaan dasar format method str
print('Kami adalah {} yang mengatakan "{}!"'.format('murid', 'lol'))

# <---Kurung dan karakter di dalamnya (disebut field format) digantikan dengan objek yang diteruskan ke metode str.format(). Sebuah angka dalam kurung dapat digunakan untuk merujuk pada posisi objek yang diteruskan ke metode str.format():
print('{0} dan {1}'.format('spam', 'telur'))
print('{1} dan {0}'.format('ucup', 'asep'))


# <---Jika argumen kata kunci digunakan dalam metode str.format(), nilai-nilainya dirujuk dengan menggunakan keyword argumen:
print('Ini {makanan} adalah {deskripsi}.'.format(makanan="telur", deskripsi='enak'))

# <--kombinasi dari semuanya
# print('hai {} saya {nama}, tinggal {0}'.format("SBY","ucup",nama="imron")) jangan seperti ini
print('hai {1} saya {nama}, tinggal {0}'.format("SBY","ucup",nama="imron")) 

# Jika Anda memiliki string format yang sangat panjang dan tidak ingin membaginya, akan lebih baik jika Anda dapat merujuk variabel yang akan diformat dengan nama alih-alih posisi. Ini dapat dilakukan dengan melewatkan dict dan menggunakan kurung siku '[]' untuk mengakses kunci.

data_dict = {"nama":"imron","alamat":"SBY","negara":"INDONESIA","no":20,"biner":90}
print("\nnama: {0[nama]:10}\nalamat: {0[alamat]:10}\nnegara: {0[negara]:10}\nno: {0[no]:x}\nbiner: {0[biner]:b}".format(data_dict))

# Ini juga dapat dilakukan dengan melewatkan dictionary tabel sebagai argumen kata kunci dengan notasi **.
tabel = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('\nJack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**tabel))

# Ini sangat berguna dalam kombinasi dengan fungsi built-in vars(), yang mengembalikan dictionary yang berisi semua variabel lokal:
tabel = {k:str(v) for k,v in vars().items()}
pesan = " ".join([f"\n{k}: " + "{" + k + "} end" for k in tabel.keys()])
print(pesan.format(**tabel)) # mengambil beberapa kwarg dari tabel

# Sebagai contoh, baris berikut menghasilkan set kolom yang teratur yang memberikan bilangan bulat serta kuadrat dan kubusnya:

for i in range(1,10):
    print('{0:2d} {1:4d} {2:6d}'.format(i,i*i,i*i*i))