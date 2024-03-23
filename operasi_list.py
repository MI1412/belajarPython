# operasi list
data_angka = [1,2,3,4,5,8,9,10,6,7,8]
print(f"data angka \n{data_angka}")

# count data / menghitung data dalam list
jumlah_data4 = data_angka.count(4)
jumlah_data3 = data_angka.count(3)
print(f"jumlah angka 4 = {jumlah_data4}")
print(f"jumlah angka 3 = {jumlah_data3}")

# menghitung posisi data dalam list

data = ["joko","ucup","denis","amir"]
print(f"data = {data}")

data_joko = data.index("joko")
print(f"posisi data joko adalah {data_joko}")

# mengurutkan list dari kecil kebesar
print(f"data angka sebelum disort {data_angka}")
data_angka.sort()
print(f"data angka yang disorting {data_angka}")
print(f"data = {data}")
data.sort()
print(f"data disort = {data}")

# mengurutkan secara terbalik
data_angka.reverse()
data.reverse()
print(f"data direserve {data}")
print(f"data angka direserve {data_angka}")


# menyalin list
a = ["joko","denis","amir"]
print(f"a = {a}")

b = a # ini bukan menyalin data list tapi memberikan referensi dari b
print(f"b = {b}")


# merubah member dari a
# ini akan merubah kedua list
a[1] = "mort"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# alamat dari kedua list a dan b
print(f"alamat a = {hex(id(a))}")
print(f"alamat b = {hex(id(b))}")

# menyalin list c dengan method copy() 

c = a.copy() # ini akan membuat list baru dengan alamat berbeda
print(f"alamat a = {hex(id(a))}")
print(f"alamat b = {hex(id(b))}")
print(f"alamat c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print("\nkita ubah data 1")
c[1] = "mamang"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")