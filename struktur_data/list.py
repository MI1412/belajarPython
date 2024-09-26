# list mempunyai semacam method, ini daftar method dari objek list:
data = []
iterable = [1,2,3]
print(f"data: {data}")
# append(data) = memasukkan data ke list
# sama seperti data[len(data):] = [x]
data.append(9)
data.append(0)
print(f"data {data}")

# extend(iterable) = menambahkan data objek iterable
# sama seperti: data[len(data):] = iterable
data.extend({121,122,124,5,6})
print(data)

# insert(index,data) = memasukkan item dengan posisi yang diberikan
# argumen pertama index dari elemen sebelum yang dimasukkan
# jadi data.insert(0, x) memasukkan data ke depan list dan a.insert(len(a), x) ini sama seperti a.append(x)
data.insert(0,'diubah')
print(f"data:  {data}")

# remove(data) = menghapus data di list menggunakan nilainya
# jika tidak ada data ditemukan akan menaikkan valueError: baca selengkapnya di exception value error
data.remove(0)
print(f"data: {data}")

# pop(index) = menghapus item dari posisi menggunakan index
# akan menaikkan indexError jika list kosong atau index tidak ada
pop = data.pop(0) 
print(f"pop: {pop}")
print(f"data: {data}")

# clear() = menghapus semua item di list 
# sama seperti del data[:] / del data
# clear = data.clear()
# print(f"clear {clear}")

# index(data[start, end]) = menampilkan index diantara data
# menaikkan valueerror jika data tidak ada
# hati hati pada saat mencoba input di terminal, akan mengembalikan string
# user_input = int(input("cari: "))
# cari_data = data.index(user_input,0,6)
# print(f"cari data {cari_data}")

# data.count(value) = menghitung data list yang sama
contoh_count = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,12,1,2,3,4,5]
count = contoh_count.count(8)
print(f"count: {count}")

# data.sort(*, key=None, reverse=False) = mengurutkan data
# lihat selengkapnya di sorted().py
list_nama= ['abbyan','imron','ucup']
list_nama.sort(key=len,reverse=False) # diurutkan berdasarkan panjang dan diurutkan terbalik
data.sort(reverse=True) # diurutkan terbalik
print(f"list nama diurut: {list_nama}")
print(f"data: {data}")

# data.reversed() = mengembalikan tempat beberapa elemen dalam list seperti aslinya
data.reverse()
print(f"reverse {data}")

# data.copy() = menyalin referensi list
copy = data.copy()
print(f"copy: {copy}")